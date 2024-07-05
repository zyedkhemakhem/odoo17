FROM odoo:17.0
EXPOSE 8069
RUN pip3 install ptvsd
USER odoo
COPY ./config/odoo.conf /etc/odoo/odoo.conf
CMD ["odoo"]
