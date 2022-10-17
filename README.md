# orderly-bot

A bot for creating orderly.server and orderly-web PRs from orderly and orderly.server updates (respectively)

This bot will

1. When there is a new PR in orderly (not yet implemented)
   1. Create a new branch in orderly.server called server-<branch-name>
   1. Update the version of orderly.server in the DESCRIPTION
   1. Pin the orderly version used by orderly.server to the branch of the new PR
   1. Create a PR for the new orderly.server branch with a link in the message to the orderly PR
1. When an existing orderly PR has a new commit (not yet implemented)
   1. Trigger a new build of the corresponding orderly.server PR
1. When an orderly.server PR with a paired orderly PR passes or fails CI checks (not yet implemented)
   1. Notify the orderly PR that orderly.server check completed successfully
1. When there is a new PR in orderly.server (not yet implemented)
   1. Create a new branch in orderly-web called web-<branch-name>
   1. Update the version of orderly-web
   1. Pin the orderly.server version used by orderly-web to the branch of the new PR
   1. Create a PR for the new orderly-web branch with a link in the message to the orderly.server PR
1. When an existing orderly.server PR has a new commit (not yet implemented)
   1. Trigger a new build of the corresponding orderly-web PR
1. When an orderly-web PR with a paired orderly.server PR passes or fails CI checks (not yet implemented)
   1. Notify the orderly.server PR that orderly-web check completed successfully

## Running

To run the service locally use the docker image

`./docker/run`

You may have to build first, if so

`./docker/build`

## Deploying

To deploy
1. ssh onto support `ssh montagu@support.montagu.dide.ic.ac.uk`
1. `cd orderly-bot`
1. Stop orderly-bot docker container
1. Run `./docker/run`

## Testing

The test use pytest and can be run by calling `pytest` from the repository root.
