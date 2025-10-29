#!/usr/bin/env python

from lib.gitlab import GitlabIssuesAPI


class GitlabIssueClose(GitlabIssuesAPI):

    def run(self, url, project, issue_iid, token, verify_ssl):
        self.url = url or self.url
        self.verify_ssl = verify_ssl or self.verify_ssl
        self.token = token or self.token

        issue = self.close(self.url, project, issue_iid)

        # Return formatted response
        result = {
            'id': issue.get('iid'),
            'global_id': issue.get('id'),
            'title': issue.get('title'),
            'state': issue.get('state'),
            'web_url': issue.get('web_url'),
            'updated_at': issue.get('updated_at'),
            'closed_at': issue.get('closed_at')
        }

        return True, result
