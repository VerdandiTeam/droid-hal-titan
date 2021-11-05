# These and other macros are documented in dhd/droid-hal-device.inc

%define device titan
%define vendor motorola

%define vendor_pretty Motorola
%define device_pretty Moto G (2nd Gen.)

%define installable_zip 1

%define straggler_files \
/init.mmi.boot.sh\
/init.mmi.touch.sh\
/init.qcom.ssr.sh\
   /selinux_version\
   /service_contexts\
%{nil}

# Entries migrated from the old rpm/droid-hal-titan.spec
%define android_config \
#define QCOM_BSP 1\
%{nil}
%define __provides_exclude_from ^/system/.*$
%define __requires_exclude ^/system/bin/.*$
%define __find_provides %{nil}
%define __find_requires %{nil}
%define additional_post_scripts \
/usr/bin/groupadd-user inet || :\
%{nil}

%include rpm/dhd/droid-hal-device.inc
