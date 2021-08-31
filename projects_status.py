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


    def _api_get_list(self, url, params=None):
        # Should handle pagination, etc
        headers = {
            'Authorization': f'Bearer {self.account_token}',
            'Harvest-Account-ID': self.account_id,
            'User-Agent': 'Project Tracking Email (mark@condense.com.au)',
        }
        res = requests.get(url, headers=headers, params=params)
        return res.json

    def my_projects(self):
        response = self._api_get_list('https://api.harvestapp.com/api/v2/users/me/project_assignments')
        assignments = response.project_assignments
        mine = [assignment for assignment in assignments if assignment.project.is_billable]
        return [assignment.project for assignment in mine]

    def active_projects(self):
        response = self._api_get_list('https://api.harvestapp.com/v2/reports/project_budget',
                                      params={'is_active': 'true'})
        return response.results


if __name__ == '__main__':
    print('Hello world')
    # main()
