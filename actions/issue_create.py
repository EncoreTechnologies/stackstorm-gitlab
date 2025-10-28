#!/usr/bin/env python

from lib.gitlab import GitlabIssuesAPI


class GitlabIssueCreate(GitlabIssuesAPI):

    def run(self, url, project, title, description, assignee_ids, labels, token, verify_ssl):
        self.url = url or self.url
        self.verify_ssl = verify_ssl or self.verify_ssl
        self.token = token or self.token

        # Parse assignee_ids if provided as comma-separated string
        parsed_assignee_ids = None
        if assignee_ids:
            if isinstance(assignee_ids, str):
                parsed_assignee_ids = [int(aid.strip()) for aid in assignee_ids.split(',')]
            elif isinstance(assignee_ids, list):
                parsed_assignee_ids = [int(aid) for aid in assignee_ids]

        # Parse labels if provided as comma-separated string
        parsed_labels = None
        if labels:
            if isinstance(labels, str):
                parsed_labels = [label.strip() for label in labels.split(',')]
            elif isinstance(labels, list):
                parsed_labels = labels

        issue = self.create(
            self.url,
            project,
            title,
            description=description,
            assignee_ids=parsed_assignee_ids,
            labels=parsed_labels
        )

        # Return formatted response
        result = {
            'id': issue.get('iid'),
            'global_id': issue.get('id'),
            'title': issue.get('title'),
            'description': issue.get('description'),
            'state': issue.get('state'),
            'web_url': issue.get('web_url'),
            'created_at': issue.get('created_at')
        }

        return True, result
