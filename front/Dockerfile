FROM node:lts-buster AS development

# permissions and nonroot user for tightened security
RUN adduser app

WORKDIR /home/app
USER app


COPY --chown=app:app calculator_react .

RUN npm i

CMD ["npm", "start"]

EXPOSE 3000

