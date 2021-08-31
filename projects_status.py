#!/usr/bin/env python
import os
import requests


class Config:
    def __init__(self, envdict=None):
        super().__init__()
        if not envdict:
            envdict = os.environ
        self._load(envdict)

    def _load(self, envdict):
        # Throw a KeyError if configuration isn't set:
        self.account_id = envdict['ACCOUNT_ID']
        self.account_token = envdict['ACCOUNT_TOKEN']
        self.account_user_id = envdict['ACCOUNT_USER_ID']
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
        assignments = self._api_get_list('https://api.harvestapp.com/api/v2/users/me/project_assignments',
                                      results_key='project_assignments')
        mine = [assignment for assignment in assignments if assignment['project']['is_billable']]
        return [assignment['project'] for assignment in mine]

    def active_projects(self):
        active = self._api_get_list('https://api.harvestapp.com/v2/reports/project_budget',
                                      results_key='results',
                                      params={'is_active': 'true'})
        return active


if __name__ == '__main__':
    print('Hello world')
    # main()
