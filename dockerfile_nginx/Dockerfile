FROM nginx:1.19-alpine

# Run as non-root user
RUN apk add --no-cache shadow && \
    usermod -u 1000 nginx && \
    groupmod -g 1000 nginx && \
    apk del shadow

# Create necessary directories with correct permissions
RUN mkdir -p /var/cache/nginx/client_temp && \
    chown -R nginx:nginx /var/cache/nginx && \
    chown -R nginx:nginx /var/log/nginx && \
    chown -R nginx:nginx /etc/nginx && \
    chmod -R 755 /var/cache/nginx && \
    touch /var/run/nginx.pid && \
    chown nginx:nginx /var/run/nginx.pid

# Remove default configuration and unnecessary files
RUN rm -rf /etc/nginx/conf.d/default.conf && \
    rm -f /docker-entrypoint.d/10-listen-on-ipv6-by-default.sh

COPY nginx.conf /etc/nginx/nginx.conf
COPY conf.d/ /etc/nginx/conf.d/

USER nginx

EXPOSE 8080 8443

ENTRYPOINT ["nginx"]
CMD ["-g", "daemon off;"]
