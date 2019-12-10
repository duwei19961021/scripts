FROM docker.io/ubuntu:18.04
RUN export DEBIAN_FRONTEND=noninteractive \
    && apt-get update -y \
    && apt-get -y install tzdata net-tools telnet curl telnet inetutils-ping wget build-essential libtool gcc automake autoconf make \
    && for i in nginx-1.16.1.tar.gz openssl-1.0.2o.tar.gz pcre-8.40.tar.gz zlib-1.2.11.tar.gz;do wget    http://172.17.62.15:/$i;tar xf $i -C /usr/local/src ;done \
    && useradd -M -s /sbin/nologin www \
    && cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
    && cd /usr/local/src/pcre-8.40 \
    && ./configure \
    && make \
    && make install \
    && cd /usr/local/src/zlib-1.2.11 \
    && ./configure \
    && make \
    && make install \
    && cd /usr/local/src/openssl-1.0.2o \
    && ./config \
    && make \
    && make install \
    && cd /usr/local/src/nginx-1.16.1/ \
    && ./configure --sbin-path=/usr/sbin/nginx \
                   --conf-path=/etc/nginx/nginx.conf \
                   --pid-path=/var/run/nginx.pid \
                   --with-http_ssl_module \
                   --with-pcre=/usr/local/src/pcre-8.40 \
                   --with-zlib=/usr/local/src/zlib-1.2.11 \
                   --with-openssl=/usr/local/src/openssl-1.0.2o \
                   --prefix=/data/wwwroot \
                   --error-log-path=/var/log/nginx/error.log \
                   --http-log-path=/var/log/nginx/access.log \
                   --lock-path=/var/run/nginx.lock \
                   --with-http_realip_module \
                   --with-http_gunzip_module \
                   --with-http_gzip_static_module \
                   --with-http_stub_status_module \
                   --modules-path=/usr/lib/nginx/modules \
                   --conf-path=/etc/nginx/nginx.conf \
                   --http-client-body-temp-path=/var/cache/nginx/client_temp \
                   --http-proxy-temp-path=/var/cache/nginx/proxy_temp \
                   --http-fastcgi-temp-path=/var/cache/nginx/fastcgi_temp \
                   --http-uwsgi-temp-path=/var/cache/nginx/uwsgi_temp \
                   --http-scgi-temp-path=/var/cache/nginx/scgi_temp \
                   --with-stream \
                   --with-stream_ssl_module \
    && make \
    && make install \
    && mkdir /var/cache/nginx/uwsgi_tem -p \
    && mkdir /var/cache/nginx/client_temp \
    && mkdir /var/cache/nginx/proxy_temp \
    && mkdir /var/cache/nginx/scgi_temp \
    && mkdir /var/cache/nginx/fastcgi_temp \
    && mkdir /etc/nginx/conf.d \
    && apt-get -y remove wget build-essential libtool gcc automake autoconf make \
    && apt -y autoremove && apt-get clean  &&rm -rf /usr/local/src/* \
    && rm -rf /*.gz \
    && ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log
#VOLUME /var/log/nginx
CMD ["nginx"]
