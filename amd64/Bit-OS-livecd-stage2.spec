subarch: amd64
target: livecd-stage2
version_stamp: Rolling
rel_type: default
profile: default/linux/amd64/23.0/hardened/selinux
snapshot: 20260718
source_subpath:
livecd/fstype: squashfs
livecd/isolabel: Bit-OS
livecd/modloop: squashfs

# Arquivo ou diretório com uma árvore de arquivos sobreposta (overlay) 
# que será copiada diretamente para a raiz (/) do LiveCD (ex: configs prontas em /etc)
livecd/root_overlay: /meus_arquivos/iso_root_overlay

# Overlay que vai especificamente para o diretório inicial do usuário do LiveCD
livecd/dev_overlay: /meus_arquivos/iso_dev_overlay

boot/kernel: gentoo

# Código fonte do kernel que o genkernel irá compilar
boot/kernel/gentoo/sources: sys-kernel/gentoo-sources

# Arquivo de configuração (.config) customizado do kernel que você quer usar
boot/kernel/gentoo/config: /meus_arquivos/kernel-config-x86_64

# Argumentos passados diretamente ao genkernel (ex: incluir suporte a ramdisk completo)
boot/kernel/gentoo/gk_mainargs: --allramdisk --multipath --luks --mdadm

# Módulos do kernel que devem ser carregados obrigatoriamente no boot inicial
boot/kernel/gentoo/modules: e1000e nouveau usb-storage

# Serviços que serão ativados automaticamente em runlevels específicos
# Formato: nome_do_servico|runlevel
livecd/rcadd:
    dbus|default
    NetworkManager|default
    xdm|default
    sshd|default

# Define qual gerenciador de boot a ISO vai usar (ex: grub, isolinux, systemd-boot)
livecd/bootargs: dockernel=gentoo root=/dev/ram0 init=/linuxrc

# Copia arquivos diretamente para a partição de boot/mídia da ISO (como temas do GRUB)
livecd/boot_overlay: /meus_arquivos/iso_boot_overlay