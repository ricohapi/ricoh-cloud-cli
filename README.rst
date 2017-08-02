=========
RICOH Cloud CLI
=========

Command line interface for RICOH Cloud API.

------------
Installation
------------
::

  $ git clone https://github.com/ricohapi/ricoh-cloud-cli.git
  $ cd ricoh-cloud-cli
  $ pip install . --find-links=git+https://github.com/ricohapi/ricoh-cloud-sdk-python.git#egg=ricoh-cloud-sdk-0.3.0

You can also download RICOH Cloud CLI in a zip file from https://github.com/ricohapi/ricoh-cloud-cli/releases and unzip it to ``<install_dir>``.

Using Python 3 on Linux
----------------------

The following settings are required in python 3 environment on Linux.

::

  [CentOS]
  $ export LANG=en_US.utf-8

  [Ubuntu]
  $ export LC_ALL=C.UTF-8
  $ export LANG=C.UTF-8

See here http://click.pocoo.org/5/python3/#python-3-surrogate-handling for technical details.

--------
Synopsis
--------
::

  rapi [global_options] <service> <command> [options options_argment]


Global Options
--------------
::

  [--profile <profile_name>]	Use the specific profile.
  [--version]			Show the version and exit.
  [-h, --help]			Show help message and exit.

Available Services
------------------

configure [--profile <profile_name>]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Configures Client Credentials
- This command prompts you for your Client Credentials.
- You can set a name on profile so that you can manage multiple Client Credentials.
- If you do not specify any ``<profile_name>``, the ``default`` profile is updated.
- You do not need ``<command>`` for this service.

vrs
~~~~~~~~~~~~~

- Accesses Visual Recognition API
- You also need to set ``<command>`` for this service.

Available Commands for vrs
--------------------------

detect_humans
~~~~~~~~~~~~~

This command sends a Human Detection request. The API detects people in specified image.

::

  [-i, --image] URI or local file path of image

detect_faces
~~~~~~~~~~~~

This command sends a Face Detection request. The API detects faces in specified image.

::

  [-i, --image] URI or local file path of image

compare_faces
~~~~~~~~~~~~~

This command sends a Face Recognition request. The API compares faces in two specified images and returns how similar the faces are.

::

  [-s, --source_image] URI or local file path of source image
  [-t, --target_image] URI or local file path of target image

-----------
Configuring
-----------

Credentials
-----------

RICOH Cloud CLI searches the following locations for Client Credentials:

1. Environment Variables – RAPI_CLIENT_ID, RAPI_CLIENT_SECRET
2. Credential file – ``~/.rapi/credentials.json`` (Linux, macOS or Unix) or ``%USERPROFILE%\.rapi\credentials.json`` (Windows). You can make a credential file by running ``rapi configure``.

Proxy
-----

To use RICOH Cloud API through proxy servers, configure HTTP_PROXY and HTTPS_PROXY environment variables with proxy IP addresses.

::

  $ export HTTP_PROXY="<HOST>:<PORT>"
  $ export HTTPS_PROXY="<HOST>:<PORT>"

------------------
Command Completion
------------------

RICOH Cloud CLI offers useful command completion. To activate it, add the following line to your .bashrc:
::

  eval "$(_RAPI_COMPLETE=source rapi)"

This command calls ``rapi`` every time when you start your shell, which might affect the start-up time. To avoid that, you can run the following command:
::

  $ _RAPI_COMPLETE=source rapi > rapi-complete.sh

And add the following line to your .bashrc:
::
  . <path_to_directory>/rapi-complete.sh

Limitation
----------
- RICOH Cloud CLI currently supports command completion only for Bash.

--------
Examples
--------
::

  $ rapi configure
  RAPI Client ID: clientId
  RAPI Client Secret: clientSecret

  $ rapi vrs compare_faces -s ./tests/images/test_3a.jpg -t ./tests/images/test_3b.jpg
  {
    "score": 0.7843703031539917,
    "source": {
      "location": {
        "top": 100,
        "right": 451,
        "bottom": 173,
        "left": 378
      }
    },
    "target": {
      "location": {
         "top": 82,
         "right": 285,
         "bottom": 140,
         "left": 227
      }
    }
  }

--------
See Also
--------

- `RICOH Cloud API Developer Guide <https://api.ricoh/docs/ricoh-cloud-api/>`_
