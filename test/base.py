#!/usr/bin/env python3

import sys
sys.path.append('..')

import coh_metrix_port as coh

t = coh.Text('The book is on the table.')
bc = coh.basic_counts.BasicCounts()

print(bc)

r = bc.values_for_text(t)
print(r)
print(r.basic_counts.flesch)
