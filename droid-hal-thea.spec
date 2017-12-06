%define device thea
%define vendor motorola
%define vendor_pretty Motorola
%define device_pretty Moto G (2nd Gen. LTE)
%define installable_zip 1

#for ota update
%define enable_kernel_update 1

%define straggler_files\
   /init.mmi.boot.sh\
   /init.mmi.touch.sh\
   /init.qcom.ssr.sh\
   /selinux_version\
   /service_contexts\
%{nil}

%include rpm/dhd/droid-hal-device.inc 
