import sys
import os

__all_ = [
    'cly_tasks', 'dj', 'dj_app_hi', 'log'
]

root_path = os.path.abspath(os.path.dirname(__file__))

sys.path.extend(
    [
        os.path.join(root_path, 'cly_tasks'),
        os.path.join(root_path, 'dj'),
        os.path.join(root_path, 'dj_app_hi'),
        os.path.join(root_path, 'log')
    ]
)
