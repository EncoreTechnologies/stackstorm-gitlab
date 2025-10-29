#!/usr/bin/env python

from lib.gitlab import GitlabIssuesAPI


class GitlabIssueList(GitlabIssuesAPI):

    def run(self, url, project, state, token, verify_ssl):
        self.url = url or self.url
        self.verify_ssl = verify_ssl or self.verify_ssl
        self.token = token or self.token

        issues = self.list(self.url, project, state=state)

        # Format the response to include name (title), ID (iid), and status (state)
        formatted_issues = []
        for issue in issues:
            formatted_issues.append({
                'name': issue.get('title'),
                'id': issue.get('iid'),
                'status': issue.get('state'),
                'web_url': issue.get('web_url'),
                'created_at': issue.get('created_at'),
                'updated_at': issue.get('updated_at')
            })

        return True, formatted_issues
