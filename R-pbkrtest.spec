#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-pbkrtest
Version  : 0.4.8.6
Release  : 68
URL      : https://cran.r-project.org/src/contrib/pbkrtest_0.4-8.6.tar.gz
Source0  : https://cran.r-project.org/src/contrib/pbkrtest_0.4-8.6.tar.gz
Summary  : Parametric Bootstrap and Kenward Roger Based Methods for Mixed Model Comparison
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-lme4
Requires: R-magrittr
BuildRequires : R-Rcpp
BuildRequires : R-lme4
BuildRequires : R-magrittr
BuildRequires : buildreq-R

%description
# pbkrtest
Parametric Bootstrap and Kenward Roger Based Methods for Mixed Model Comparison

%prep
%setup -q -c -n pbkrtest

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1582303223

%install
export SOURCE_DATE_EPOCH=1582303223
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library pbkrtest
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library pbkrtest
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library pbkrtest
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc pbkrtest || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/pbkrtest/CITATION
/usr/lib64/R/library/pbkrtest/DESCRIPTION
/usr/lib64/R/library/pbkrtest/INDEX
/usr/lib64/R/library/pbkrtest/Meta/Rd.rds
/usr/lib64/R/library/pbkrtest/Meta/data.rds
/usr/lib64/R/library/pbkrtest/Meta/features.rds
/usr/lib64/R/library/pbkrtest/Meta/hsearch.rds
/usr/lib64/R/library/pbkrtest/Meta/links.rds
/usr/lib64/R/library/pbkrtest/Meta/nsInfo.rds
/usr/lib64/R/library/pbkrtest/Meta/package.rds
/usr/lib64/R/library/pbkrtest/Meta/vignette.rds
/usr/lib64/R/library/pbkrtest/NAMESPACE
/usr/lib64/R/library/pbkrtest/NEWS
/usr/lib64/R/library/pbkrtest/R/pbkrtest
/usr/lib64/R/library/pbkrtest/R/pbkrtest.rdb
/usr/lib64/R/library/pbkrtest/R/pbkrtest.rdx
/usr/lib64/R/library/pbkrtest/data/Rdata.rdb
/usr/lib64/R/library/pbkrtest/data/Rdata.rds
/usr/lib64/R/library/pbkrtest/data/Rdata.rdx
/usr/lib64/R/library/pbkrtest/doc/index.html
/usr/lib64/R/library/pbkrtest/doc/pbkrtest.R
/usr/lib64/R/library/pbkrtest/doc/pbkrtest.Rnw
/usr/lib64/R/library/pbkrtest/doc/pbkrtest.pdf
/usr/lib64/R/library/pbkrtest/help/AnIndex
/usr/lib64/R/library/pbkrtest/help/aliases.rds
/usr/lib64/R/library/pbkrtest/help/paths.rds
/usr/lib64/R/library/pbkrtest/help/pbkrtest.rdb
/usr/lib64/R/library/pbkrtest/help/pbkrtest.rdx
/usr/lib64/R/library/pbkrtest/html/00Index.html
/usr/lib64/R/library/pbkrtest/html/R.css
