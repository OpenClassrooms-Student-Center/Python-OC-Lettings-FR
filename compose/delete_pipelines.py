import argparse
import datetime

import gitlab
import pytz
from dateutil import parser


def del_pipeline(server_url, gitlab_token, keep_days, project_id):
    gl = gitlab.Gitlab(server_url, private_token=gitlab_token)
    till = (datetime.datetime.now() - datetime.timedelta(days=int(keep_days))).replace(
        tzinfo=pytz.UTC
    )
    print(f"Clean before {till}")
    project = gl.projects.get(int(project_id))
    for pipeline in project.pipelines.list(iterator=True):
        if parser.parse(pipeline.updated_at) > till:
            continue
        print(f"Deleting {project.id}:{pipeline.id}")
        pipeline.delete()


if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser(description="Deleting pipelines arguments")
    arg_parser.add_argument("server_url")
    arg_parser.add_argument("gitlab_token")
    arg_parser.add_argument("keep_days")
    arg_parser.add_argument("project_id")
    args = arg_parser.parse_args()
    del_pipeline(args.server_url, args.gitlab_token, args.keep_days, args.project_id)
