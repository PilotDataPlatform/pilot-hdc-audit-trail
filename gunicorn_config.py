# Copyright (C) 2022-Present Indoc Systems
#
# Licensed under the GNU AFFERO GENERAL PUBLIC LICENSE,
# Version 3.0 (the "License") available at https://www.gnu.org/licenses/agpl-3.0.en.html.
# You may not use this file except in compliance with the License.

workers = 4
threads = 2
bind = '0.0.0.0:5077'
daemon = 'false'
worker_connections = 1200
accesslog = '-'
errorlog = '-'
loglevel = 'debug'
