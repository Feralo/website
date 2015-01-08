website
=======
[![Build Status](https://travis-ci.org/Feralo/website.svg?branch=master)](https://travis-ci.org/Feralo/website)

Read the [provisioning notes](deploy_tools/provisioning_notes.md) for an idea of how to get up and running quickly.

Make sure that your firewall allows http:
<code>sudo firewall-cmd --add-service=http --permanent --zone=public</code>

Check the gunicorn service file:
<code>less /usr/lib/systemd/system/[[SITENAME]].service</code>

[example site](http://feralo.com/)
