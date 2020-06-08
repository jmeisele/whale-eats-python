# Use the Nginx image
FROM nginx

# Remove the default nginx.conf
# RUN rm /etc/nginx/conf.d/default.conf 
RUN rm /etc/nginx/conf.d/default.conf; exit 0


EXPOSE 80

# Replace with our own nginx.conf
COPY nginx.conf /etc/nginx/conf.d/