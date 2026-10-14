TERMUX_PKG_HOMEPAGE=https://github.com/kennethdevon/jarvis
TERMUX_PKG_DESCRIPTION="Terminal chat assistant for Termux"
TERMUX_PKG_LICENSE="MIT"
TERMUX_PKG_MAINTAINER="Kenneth Devon <kennethdevon@users.noreply.github.com>"
TERMUX_PKG_VERSION=0.1.0
TERMUX_PKG_SRCURL="git+https://github.com/kennethdevon/jarvis.git"
TERMUX_PKG_GIT_BRANCH=main
TERMUX_PKG_DEPENDS="python"

termux_step_make_install() {
    install -Dm755 "$TERMUX_PKG_SRCDIR/data/jarvis" "$TERMUX_PREFIX/bin/jarvis"
    install -Dm644 "$TERMUX_PKG_SRCDIR/jarvis.py" "$TERMUX_PREFIX/share/jarvis/jarvis.py"
    install -Dm644 "$TERMUX_PKG_SRCDIR/README.md" "$TERMUX_PREFIX/share/doc/jarvis/README.md"
    install -Dm644 "$TERMUX_PKG_SRCDIR/LICENSE" "$TERMUX_PREFIX/share/doc/jarvis/LICENSE"
}
