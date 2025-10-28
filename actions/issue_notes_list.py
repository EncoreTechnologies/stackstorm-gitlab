#!/usr/bin/env python

from lib.gitlab import GitlabIssuesAPI


class GitlabIssueNotesList(GitlabIssuesAPI):

    def run(self, url, project, issue_iid, token, verify_ssl):
        self.url = url or self.url
        self.verify_ssl = verify_ssl or self.verify_ssl
        self.token = token or self.token

        notes = self.list_notes(self.url, project, issue_iid)

        # Format the response
        formatted_notes = []
        for note in notes:
            formatted_notes.append({
                'id': note.get('id'),
                'body': note.get('body'),
                'author': {
                    'id': note.get('author', {}).get('id'),
                    'username': note.get('author', {}).get('username'),
                    'name': note.get('author', {}).get('name')
                },
                'created_at': note.get('created_at'),
                'updated_at': note.get('updated_at'),
                'system': note.get('system', False),
                'noteable_type': note.get('noteable_type')
            })

        return True, formatted_notes
