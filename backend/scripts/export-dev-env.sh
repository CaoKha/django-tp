#!/bin/sh

## Usage:
##   . ./export-env.sh ; $COMMAND
##   . ./export-env.sh ; echo ${MINIENTREGA_FECHALIMITE}

unamestr=$(uname)
if [ "$unamestr" = 'Linux' ]; then
  export "$(grep -v '^#' env/dev/env.django.dev | xargs -d '\n')"
  export "$(grep -v '^#' env/dev/env.postgres.dev | xargs -d '\n')"
elif [ "$unamestr" = 'FreeBSD' ] || [ "$unamestr" = 'Darwin' ]; then
  export "$(grep -v '^#' env/dev/env.django.dev | xargs -0)"
  export "$(grep -v '^#' env/dev/env.postgres.dev | xargs -0)"
fi
