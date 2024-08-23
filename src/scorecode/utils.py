#
# Copyright (c) nexB Inc. and others. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# See http://www.apache.org/licenses/LICENSE-2.0 for the license text.
# See https://github.com/aboutcode-org/scorecode for support or download.
# See https://aboutcode.org for more information about nexB OSS projects.
#


def remove_fragment(url: str):
    """
    Return a URL without fragments
    """

    try:
        if url:
            return url.split("#")[0]

    except ValueError:
        return None
