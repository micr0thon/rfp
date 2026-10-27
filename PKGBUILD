# Maintainer: SPCoaky <cobaltbl00d@proton.me>
pkgname=rgfp
pkgver=1.1.0
pkgrel=1
pkgdesc="A lightweight randomized file picker built in Python."
arch=('any')
url="https://github.com/micr0thon/rgfp"
license=('AGPL-3.0-only')
depends=('python')
source=("$pkgname-$pkgver.tar.gz::$url/archive/refs/tags/v$pkgver.tar.gz")
sha256sums=('SKIP')

package() {
	cd "$pkgname-$pkgver"

	# Installs the script executable.
	install -Dm755 rgfp.py "$pkgdir/usr/bin/rgfp"

	# AGPL-3.0 thing idk
	install -Dm644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
