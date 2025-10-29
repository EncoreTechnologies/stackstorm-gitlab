#!/usr/bin/env python

import base64
from lib.gitlab import GitlabProjectsAPI


class GitlabProjectFileGet(GitlabProjectsAPI):

    def run(self, url, project, file_path, ref, decode_content,
            token, verify_ssl):
        self.url = url or self.url
        self.verify_ssl = verify_ssl or self.verify_ssl
        self.token = token or self.token

        file_data = self.get_file(self.url, project, file_path, ref=ref)

        # Return formatted response
        result = {
            'file_name': file_data.get('file_name'),
            'file_path': file_data.get('file_path'),
            'size': file_data.get('size'),
            'encoding': file_data.get('encoding'),
            'content': file_data.get('content'),
            'ref': file_data.get('ref'),
            'blob_id': file_data.get('blob_id'),
            'commit_id': file_data.get('commit_id'),
            'last_commit_id': file_data.get('last_commit_id')
        }

        # Decode base64 content if requested
        if decode_content and file_data.get('encoding') == 'base64':
            try:
                decoded_content = base64.b64decode(
                    file_data.get('content', '')
                ).decode('utf-8')
                result['content_decoded'] = decoded_content
            except Exception as e:
                result['content_decoded'] = None
                result['decode_error'] = str(e)

        return True, result
