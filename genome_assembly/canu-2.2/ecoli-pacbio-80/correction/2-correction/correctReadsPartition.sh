#!/bin/sh


#  Path to Canu.

bin="/Users/student/genome_assembly/canu-2.2/bin"

#  Report paths.

echo ""
echo "Found perl:"
echo "  " `which perl`
echo "  " `perl --version | grep version`
echo ""
echo "Found java:"
echo "  " `which /Users/student/miniconda/bin/java`
echo "  " `/Users/student/miniconda/bin/java -showversion 2>&1 | head -n 1`
echo ""
echo "Found canu:"
echo "  " $bin/canu
echo "  " `$bin/canu -version`
echo ""


#  Environment for any object storage.

export CANU_OBJECT_STORE_CLIENT=
export CANU_OBJECT_STORE_CLIENT_UA=
export CANU_OBJECT_STORE_CLIENT_DA=
export CANU_OBJECT_STORE_NAMESPACE=
export CANU_OBJECT_STORE_PROJECT=



$bin/falconsense \
  -partition 6 0.854 64 10000 \
  -S ../../ecoli-80.seqStore \
  -C ../ecoli-80.corStore \
  -R ./ecoli-80.readsToCorrect \
  -t  4 \
  -cc 0 \
  -cl 1000 \
  -oi 0.75 \
  -ol 500 \
  -p ./correctReadsPartition.WORKING \
&& \
mv ./correctReadsPartition.WORKING.batches ./correctReadsPartition.batches \
&& \
exit 0

exit 1
