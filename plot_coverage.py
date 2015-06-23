#!/usr/bin/env python

# Required configuration for some grid computing environments:
# import os
# os.environ["MPLCONFIGDIR"] = "/scratch/tmp/"
# import matplotlib
# matplotlib.use("Agg")

import numpy, sys, pylab, os.path, pysam, pandas, seaborn

RES = 10000
SKIP = 1000

def parse(sam):
    for chromo, length in zip(sam.references, sam.lengths):
        depths = numpy.zeros(length + 1)
        for base in sam.pileup(chromo, stepper="all"):
            try: # ugly hack because the API changed (?)
                depths[base.reference_pos] += base.nsegments
            except AttributeError:
                depths[base.pos] += base.nsegments
        df = pandas.DataFrame(depths, index=numpy.arange(length + 1), columns=["depth"])
        yield chromo, length, pandas.rolling_mean(df, window=RES)

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print >>sys.stderr, "usage: python %s input.bam" % sys.argv[0]
        sys.exit(1)

    seaborn.set_style("white")
    sam = pysam.Samfile(sys.argv[1])

    offset = 0
    y_text = None
    medians = {}
    all_depths = []

    with seaborn.color_palette("husl", sam.nreferences):
        for chromo, length, counts in parse(sam):
            if "Un" in chromo or "random" in chromo or "hap" in chromo or "M" in chromo or "mt" in chromo:
                continue # skip weird chromosomes
            pylab.plot(counts.index.values[::SKIP] + offset, counts[counts.columns[0]].values[::SKIP], '.')
            if y_text is None:
                y_text = numpy.median(counts[counts.columns[0]])
            pylab.text(offset + length*0.5, y_text, chromo, horizontalalignment="center", verticalalignment="center")
            offset += length

            medians[chromo] = numpy.median(counts[counts.columns[0]])
            all_depths.extend(counts[counts.columns[0]][::SKIP])

    # print normalized median coverages for aneuploidy analysis
    print "chromosome\tnormalized_coverage"
    for chromo in sam.references:
        if medians.has_key(chromo):
            print "%s\t%.4f" % (chromo, medians[chromo] / numpy.median(all_depths))

    # draw some reference lines for identifying common aneuploidies
    for mult, color, label in [(1.5, '--', "2N (+/-1)"),
                               (0.5, '--', None),
                               (2.0, '-.', "1N (+/-1)"),
                               (0.05, '-.', None),
                               (1.3333, ':', "3N (+/-1)"),
                               (0.6666, ':', None)]:
        pylab.axhline(numpy.median(all_depths) * mult, ls=color, color="k", lw=1, alpha=0.5, label=label)

    pylab.legend()
    pylab.xlabel("bp")
    pylab.ylabel("coverage (%d-bp averaged)" % RES)

    pylab.gca().set_xlim([0, offset+RES+1])
    pylab.title(sys.argv[-1])

    # pylab.show()

    pylab.gcf().set_size_inches(16,4)
    pylab.savefig("%s.depth.png" % os.path.basename(sam.filename))
