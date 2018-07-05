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
  $ pip install . --find-links=git+https://github.com/ricohapi/ricoh-cloud-sdk-python.git@v0.4.0#egg=ricoh-cloud-sdk-0.4.0

You can also download RICOH Cloud CLI as a zip file from https://github.com/ricohapi/ricoh-cloud-cli/releases and unzip it to ``<install_dir>``.

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

  rapi [global_options] <service> <command> <sub_command> [options options_argment]


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
::

  rapi [global_options] vrs <command> [options options_argment]

- Accesses Visual Recognition API
- You also need to set ``<command>`` for this service.

ips
~~~~~~~~~~~~~
::

  rapi [global_options] ips <command> <sub_command> [options options_argment]

- Accesses Image Processing API
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

This command sends a Face Recognition request. The API compares faces in two specified resources and returns how similar the faces are.

::

  [-s, --source] URI or local file path of source image
  [-t, --target] URI or local file path of target resource (image or face collection)

create_collection
~~~~~~~~~~~~~

This command sends a request to create a face collection.

list_collections
~~~~~~~~~~~~~

This command sends a request to list face collections.

delete_collection
~~~~~~~~~~~~~

This command sends a request to delete a face collection.

::

    [COLLECTION_ID] ID of the face collection.


add_face
~~~~~~~~~~~~~

This command sends a request to add a face to the face collection.

::

    [-i, --image] URI or local file path of source image
    [COLLECTION_ID] ID of the face collection.


list_faces
~~~~~~~~~~~~~

This command sends a request to list faces stored in the face collection.

::

    [COLLECTION_ID] ID of the face collection.


remove_face
~~~~~~~~~~~~~

This command sends a request for remove face from the face collection.

::

    [--face_id] ID of the face.
    [COLLECTION_ID] ID of the face collection.


Available Commands for ips
--------------------------

filter
~~~~~~~~~~~~~

- Accesses filter API of Image Processing Service
- You also need to set ``<sub_command>`` for this command.

Available Sub Commands for filter
---------------------------------

blur
~~~~~~~~~~~~~

This sub command sends a Blur Filter request. The API applies image filters to an image using a blur filter.

::

  [-i, --input <uri_or_filepath>]   Specify the image URI or local file path.
  [-o, --output <filepath>]         Write to file instead stdout.
  [-l, --location <left,top,right,bottom>
                                    Specify the location to filter with comma-separated int values.
                                    You can specify up to 100 locations, but be sure to specify at least one location.
  [--locations_shape [rectangle|min_enclosing_circle]]
                                    Specify the shape of locations.
  [--locations_edge [none|blur]]    Specify the edge of locations.
  [-k, --ksize <width,height>]      Specify the blurring kernel size with comma-separated int values.

gaussian
~~~~~~~~~~~~~

This sub command sends a Gaussian Filter request. The API applies image filters to an image using a gaussian filter.

::

  [-i, --input <uri_or_filepath>]   Specify the image URI or local file path.
  [-o, --output <filepath>]         Write to file instead stdout.
  [-l, --location <left,top,right,bottom>
                                    Specify the location to filter with comma-separated int values.
                                    You can specify up to 100 locations, but be sure to specify at least one location.
  [--locations_shape [rectangle|min_enclosing_circle]]
                                    Specify the shape of locations.
  [--locations_edge [none|blur]]    Specify the edge of locations.
  [-k, --ksize <width,height>]      Specify the gaussian kernel size with comma-separated int values.
  [-s, --sigma <x,y>]               Specify the gaussian kernel standard deviation with comma-separated float values.

median
~~~~~~~~~~~~~

This sub command sends a Median Filter request. The API applies image filters to an image using a median filter.

::

  [-i, --input <uri_or_filepath>]   Specify the image URI or local file path.
  [-o, --output <filepath>]         Write to file instead stdout.
  [-l, --location <left,top,right,bottom>
                                    Specify the location to filter with comma-separated int values.
                                    You can specify up to 100 locations, but be sure to specify at least one location.
  [--locations_shape [rectangle|min_enclosing_circle]]
                                    Specify the shape of locations.
  [--locations_edge [none|blur]]    Specify the edge of locations.
  [-k, --ksize <size>]              Specify the kernel size with int value.

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
