#!/usr/bin/env python
import os

from mako.template import Template
import requests


class HarvestAPI:
    def __init__(self, envdict=None):
        super().__init__()
        if not envdict:
            envdict = os.environ
        self._load(envdict)

    def _load(self, envdict):
        # Throw a KeyError if configuration isn't set:
        self.account_id = envdict['HARVEST_ID']
        self.account_token = envdict['HARVEST_TOKEN']
        self.account_email = envdict['ACCOUNT_EMAIL']


    def _api_get_list(self, url, results_key, params=None):
        data = []
        while True:
            headers = {
                'Authorization': f'Bearer {self.account_token}',
                'Harvest-Account-ID': self.account_id,
                'User-Agent': f'Project Tracking Email ({self.account_email})',
            }
            res = requests.get(url, headers=headers, params=params).json()
            data.extend(res[results_key])
            if res.get('next'):
                url = res['links']['next']
            else:
                break
        return data

    def my_projects(self):
        """Returns a list of projects the currently-authenticated user
        is assigned to.  Useful for interactive testing."""
        assignments = self._api_get_list('https://api.harvestapp.com/api/v2/users/me/project_assignments',
                                      results_key='project_assignments')
        mine = [assignment['project'] for assignment in assignments
                if assignment['project']['is_billable']]
        return mine

    def active_projects(self):
        """Returns a list of active projects.  Useful for interactive
        testing."""
        active = self._api_get_list('https://api.harvestapp.com/v2/reports/project_budget',
                                      results_key='results',
                                      params={'is_active': 'true'})
        return active

    def load_and_prioritise(self):
        """Main data entry point; returns a list of projects in order
        of most-to-least urgent"""
        my_ids = set(project['id'] for project in self.my_projects())
        # Want sorted by mine, then by budget "hotness"
        projects = [dict(project, mine=project['project_id'] in my_ids)
                    for project in self.active_projects()]
        prioritised = sorted(projects,
                             key=lambda p: (not p['mine'], p['budget_remaining'] / p['budget']))
        return prioritised


def enrich_data(projects):
    """Placeholder for now; thinking is to add styling like 'red for
    getting hot', without calculating that in the template"""
    return projects


def format_email(projects):
    tmpl = Template(filename="email.tpl")
    txt = tmpl.render(projects=projects)
    return txt


def main():
    api = HarvestAPI()
    projects = api.load_and_prioritise()
    projects = enrich_data(projects)
    txt = format_email(projects)
    with open('email.html', 'w') as f:
        f.write(txt)


if __name__ == '__main__':
    main()
