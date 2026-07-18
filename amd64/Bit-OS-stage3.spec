subarch: amd64
target: stage3
version_stamp: rolling
rel_type: default
profile: default/linux/amd64/23.0/hardened/selinux
snapshot: 20260718
source_subpath: default/stage3-amd64-desktop-latest

# Altera a variável CFLAGS dentro do ambiente de build
stage3/cflags: -O2 -pipe -march=x86-64

stage3/use: -plasma mls -gnome -X -wayland selinux networkmanager -systemd verify-sig

stage3/packages:
    dev-lang/python
    sys-libs/libsepol
    sys-libs/libselinux
    sys-libs/libsemanage
    sys-apps/checkpolicy
    sys-apps/policycoreutils
    sec-policy/selinux-base-policy


stage3/unmerge:
    sys-apps/sed

# Diretórios que serão esvaziados (limpos) para economizar espaço no tarball final
stage3/empty:
    /var/tmp
    /var/cache
    /usr/portage/distfiles

# Arquivos ou diretórios que serão completamente deletados do tarball final
stage3/rm:
    /etc/resolv.conf