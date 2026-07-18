# =====================================================================
# CONFIGURAÇÕES BÁSICAS E DE FLUXO
# =====================================================================
subarch: amd64
target: livecd-stage1
version_stamp: personalizada-2026.0
rel_type: default
profile: default/linux/amd64/23.0/desktop
snapshot: 20260718
source_subpath: default/stage3-amd64-personalizada-2026.0

# =====================================================================
# CONFIGURAÇÕES DO PORTAGE (ESPECÍFICAS DO LIVECD)
# =====================================================================
# Flags USE adicionais ou modificadas apenas para compilar as ferramentas do LiveCD
livecd/use: livecd branding accessibility

# =====================================================================
# SELEÇÃO DE SOFTWARE DA ISO
# =====================================================================
# Todos os pacotes, ambientes gráficos e drivers que farão parte do LiveCD
livecd/packages:
    x11-base/xorg-server
    xfce-base/xfce4-meta
    sys-boot/grub
    app-admin/sudo
     net-misc/dhcpcd

# =====================================================================
# CUSTOMIZAÇÃO DE COMPILAÇÃO
# =====================================================================
# Modificações temporárias de CFLAGS para este estágio, se necessário
livecd/cflags: -O2 -pipe
livecd/cxxflags: -O2 -pipe