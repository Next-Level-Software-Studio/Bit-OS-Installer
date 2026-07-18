
subarch: amd64
target: livecd-stage2
version_stamp: personalizada-2026.0
rel_type: default
profile: default/linux/amd64/23.0/desktop
snapshot: 20260718
source_subpath: default/livecd-stage1-amd64-personalizada-2026.0

# =====================================================================
# SISTEMA DE ARQUIVOS E RÓTULOS DA MÍDIA
# =====================================================================
# Tipo de sistema de arquivos interno (geralmente squashfs)
livecd/fstype: squashfs

# Nome do volume/rótulo da ISO (Label)
livecd/isolabel: Gentoo_Custom_2026

# Tipo de loop de módulos para o boot (squashfs é o padrão)
livecd/modloop: squashfs

# Arquivo ou diretório com uma árvore de arquivos sobreposta (overlay) 
# que será copiada diretamente para a raiz (/) do LiveCD (ex: configs prontas em /etc)
livecd/root_overlay: /meus_arquivos/iso_root_overlay

# Overlay que vai especificamente para o diretório inicial do usuário do LiveCD
livecd/dev_overlay: /meus_arquivos/iso_dev_overlay

# =====================================================================
# CONFIGURAÇÃO DO(S) KERNEL(S)
# =====================================================================
# Nome do kernel padrão a ser gerado (pode listar múltiplos nomes separados por espaço)
boot/kernel: gentoo

# Código fonte do kernel que o genkernel irá compilar
boot/kernel/gentoo/sources: sys-kernel/gentoo-sources

# Arquivo de configuração (.config) customizado do kernel que você quer usar
boot/kernel/gentoo/config: /meus_arquivos/kernel-config-x86_64

# Argumentos passados diretamente ao genkernel (ex: incluir suporte a ramdisk completo)
boot/kernel/gentoo/gk_mainargs: --allramdisk --multipath --luks --mdadm

# Módulos do kernel que devem ser carregados obrigatoriamente no boot inicial
boot/kernel/gentoo/modules: e1000e nouveau usb-storage

# Módulos que devem ser colocados em uma lista negra (blacklist) para não carregarem
boot/kernel/gentoo/modblacklist: pcspkr

# =====================================================================
# INICIALIZAÇÃO E SERVIÇOS (GEREALMENTE OPENRC)
# =====================================================================
# Serviços que serão ativados automaticamente em runlevels específicos
# Formato: nome_do_servico|runlevel
livecd/rcadd:
    dbus|default
    NetworkManager|default
    xdm|default
    sshd|default

# Serviços que serão explicitamente desativados/removidos de runlevels
livecd/rcdel:
    net.lo|default

# =====================================================================
# LIMPEZA E CONFIGURAÇÕES FINAIS DO SISTEMA
# =====================================================================
# Pacotes deletados antes de fechar a ISO para reduzir o tamanho final
livecd/unmerge: acl attr bzip2 perl

# Diretórios que serão completamente esvaziados na ISO final
livecd/empty: /var/tmp /var/cache /usr/portage/distfiles /var/log

# Arquivos ou caminhos exatos que serão deletados da ISO final
livecd/rm: /etc/portage/make.profile /var/log/emerge.log

# =====================================================================
# CUSTOMIZAÇÃO VISUAL E INICIALIZAÇÃO DA ISO
# =====================================================================
# Script bash customizado que o Catalyst roda logo antes de gerar a ISO (para tweaks finos)
livecd/fsscript: /meus_arquivos/meu_script_pos_instalacao.sh

# Altera a mensagem exibida na tela de boot (se o gerenciador de boot suportar)
livecd/motd: /meus_arquivos/meu_motd_customizado

# Define qual gerenciador de boot a ISO vai usar (ex: grub, isolinux, systemd-boot)
livecd/bootargs: dockernel=gentoo root=/dev/ram0 init=/linuxrc

# Copia arquivos diretamente para a partição de boot/mídia da ISO (como temas do GRUB)
livecd/boot_overlay: /meus_arquivos/iso_boot_overlay