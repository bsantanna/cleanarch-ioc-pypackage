#!/usr/bin/env bash
(SOURCE_DIR=$(basename $PWD) ZIP=hexagonal-pypackage.zip && \
pushd .. && \
zip -r $ZIP $SOURCE_DIR --exclude $SOURCE_DIR/$ZIP --quiet && \
mv $ZIP $SOURCE_DIR/$ZIP && \
popd && \
echo "Cookiecutter full path: $PWD/$ZIP")
