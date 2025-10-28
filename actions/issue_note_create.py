#!/usr/bin/env python

from lib.gitlab import GitlabIssuesAPI


class GitlabIssueNoteCreate(GitlabIssuesAPI):

    def run(self, url, project, issue_iid, body, token, verify_ssl):
        self.url = url or self.url
        self.verify_ssl = verify_ssl or self.verify_ssl
        self.token = token or self.token

        note = self.create_note(self.url, project, issue_iid, body)

        # Return formatted response
        result = {
            'id': note.get('id'),
            'body': note.get('body'),
            'author': {
                'id': note.get('author', {}).get('id'),
                'username': note.get('author', {}).get('username'),
                'name': note.get('author', {}).get('name')
            },
            'created_at': note.get('created_at'),
            'noteable_type': note.get('noteable_type'),
            'noteable_iid': note.get('noteable_iid')
        }

        return True, result
