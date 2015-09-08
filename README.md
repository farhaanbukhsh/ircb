# ircb

A versatile IRC bouncer.


## Setup
- Install Python3 and Python3 development packages for your distro, if not already there.
  In Fedora, it'd be: ``sudo dnf install -y python3 python3-devel``
- Install dependencies: ``pip3 install -r requirements.txt``
- Copy and extend ``ircb/config/default_settings.py``, as needed, to a custom
  location. say, ``/etc/ircb/settings.py``.
- [OPTIONAL] ``export IRCB_SETTINGS=<path to your custom settings file>``

## Setting up data
- Creating a user: ``python3 manage.py createuser --username <your username> --email <your email> --password <your password>``
- Creating a network for a user:

  ```
  python3 manage.py createnetwork --user <ircb username> --name <name of network> --nick <some nick> --host <IRC server host> --port <IRC server port>
  ```
  You'll get an access token as an output of the above. Use this as
  **server password** when configuring your IRC client to connect to ``ircb``.

## Running the app

```
python3 ircb/bouncer.py
```

## Connecting for IRC client

Now, you should be able to connect to ``ircb`` from your IRC client at:
- host/port: ``localhost/9000``
- server password: <your network access token>``
