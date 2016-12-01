import os
import json
from urllib.request import urlopen


def move_docs(tag):
    stuffs = [
        'example-example',
        'example-sklearn',
        'example-msmbuilder',
        'docs',
    ]
    os.mkdir('dist/{}'.format(tag))
    for stuff in stuffs:
        os.rename('dist/{}'.format(stuff), 'dist/{}/{}'.format(tag, stuff))


def update_versions_json(base_url, tag, versions_json_fn='versions.json'):
    url = '{base_url}/{versions_json_fn}'.format(base_url=base_url, versions_json_fn=versions_json_fn)
    data = urlopen(url).read().decode()
    versions = json.loads(data)

    # new release so all the others are now old
    for i in range(len(versions)):
        versions[i]['latest'] = False

    versions.append({
        'version': tag,
        'display': '.'.join(tag.split('.')[:2]),
        'url': "{base_url}/{version}/docs/".format(base_url=base_url, version=tag),
        'latest': True,
    })
    with open("dist/versions.json", 'w') as versionf:
        json.dump(versions, versionf, indent=2)


def main():
    if not ('TRAVIS_TAG' in os.environ and len(os.environ['TRAVIS_TAG']) > 0):
        # Development version
        move_docs('dev')
    else:
        # Tagged version
        tag = os.environ['TRAVIS_TAG']
        move_docs(tag)
        update_versions_json('sphinx-modern-theme.s3-website-us-west-1.amazonaws.com/docs', tag)


main()
