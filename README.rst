Getting started
===============

.. code-block:: shell

  git clone git@github.com:unisport/dev_blog.git
  docker-compose up
  docker-compose exec dev_blog make regenerate

Now browse to http://localhost:3010/

You can read more about writing content `here <http://docs.getpelican.com/en/stable/content.html>`_

Deploying
=========

.. code-block:: shell

  docker-compose exec dev_blog make s3_upload
