FROM python:3.10-alpine AS builder

RUN pip install --upgrade pip

# permissions and nonroot user for tightened security
RUN adduser -D app
RUN mkdir -p /home/app/ && chown -R app:app /home/app
RUN mkdir -p /var/log/web && touch /var/log/web/web.err.log && touch /var/log/web/web.out.log
RUN chown -R app:app /var/log/web
WORKDIR /home/app
USER app

ENV VIRTUAL_ENV=/home/app/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY --chown=app:app . .

RUN pip3 install --upgrade pip && \
  python3 -m venv $VIRTUAL_ENV && \
  ${VIRTUAL_ENV}/bin/pip3 install -r requirements.txt && \
    ls


#ENTRYPOINT ["/env/bin/gunicorn"]
ENTRYPOINT ["/home/app/venv/bin/gunicorn"]
CMD ["-b", "0.0.0.0:8000", "wsgi:app"]
#CMD ["/"]

EXPOSE 8000

