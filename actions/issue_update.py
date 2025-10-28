#!/usr/bin/env python

from lib.gitlab import GitlabIssuesAPI


class GitlabIssueUpdate(GitlabIssuesAPI):

    def run(self, url, project, issue_iid, title, description, assignee_ids, labels, token, verify_ssl):
        self.url = url or self.url
        self.verify_ssl = verify_ssl or self.verify_ssl
        self.token = token or self.token

        # Parse assignee_ids if provided as comma-separated string
        parsed_assignee_ids = None
        if assignee_ids is not None:
            if isinstance(assignee_ids, str):
                if assignee_ids.strip():  # Only parse if not empty string
                    parsed_assignee_ids = [int(aid.strip()) for aid in assignee_ids.split(',')]
                else:
                    parsed_assignee_ids = []  # Empty list clears assignees
            elif isinstance(assignee_ids, list):
                parsed_assignee_ids = [int(aid) for aid in assignee_ids]

        # Parse labels if provided as comma-separated string
        parsed_labels = None
        if labels is not None:
            if isinstance(labels, str):
                if labels.strip():  # Only parse if not empty string
                    parsed_labels = [label.strip() for label in labels.split(',')]
                else:
                    parsed_labels = []  # Empty list clears labels
            elif isinstance(labels, list):
                parsed_labels = labels

        issue = self.update(
            self.url,
            project,
            issue_iid,
            title=title,
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
            'updated_at': issue.get('updated_at')
        }

        return True, result
