import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import numpy as np
import yaml
import os

def autotune_time(property):
    x1,y1,z1,_,_ = np.genfromtxt(os.path.dirname(__file__) + '/data/goblint_' + property + '_timings.txt', delimiter=',', unpack=True, dtype=None)
    x2,y2,z2, _, _, _, _ = np.genfromtxt(os.path.dirname(__file__) + '/data/autotune_' + property + '_timings.txt', delimiter=',', unpack=True, dtype=None)
    new_z1, new_z2 = zip(*sorted(zip(z1,z2)))
    print(np.average(z1))
    print(np.average(z2))
    print(np.sum(z1))
    print(np.sum(z2))
    print(np.average(new_z1[-10:]))
    print(np.average(new_z2[-10:]))

def goblint_stats(property):
    x1,y1,z1,result,verdict = np.genfromtxt(os.path.dirname(__file__) + '/data/goblint_' + property + '_timings.txt', delimiter=',', unpack=True, dtype=None)
    newz, newf= zip(*sorted(zip(z1,x1)))
    print("Goblint average: " + str(np.average(z1)))
    print("Goblint average 10 slowest: " + str(np.average(newz[-10:])))

    gob_true_correct = 0
    gob_false_correct = 0
    gob_true_incorrect = 0
    gob_false_incorrect = 0
    gob_unknown = result.tolist().count("unknown")
    gob_empty = result.tolist().count("empty")

    for i in range(len(result)):
        if result[i] == "True":
            if str(verdict[i]) == result[i]:
                gob_true_correct += 1
            else:
                gob_true_incorrect += 1
        elif result[i] == "False":
            if str(verdict[i]) == result[i]:
                gob_false_correct += 1
            else:
                gob_false_incorrect += 1

    print("Goblint correct true answers: " + str(gob_true_correct))
    print("Goblint correct false answers: " + str(gob_false_correct))
    print("Goblint incorrect true answers: " + str(gob_true_incorrect))
    print("Goblint incorrect false answers: " + str(gob_false_incorrect))
    print("Goblint unknown answers: " + str(gob_unknown))
    print("Goblint empty answers: " + str(gob_empty))

def conflist_stats(property):
    x1,y1,z1,_,_ = np.genfromtxt(os.path.dirname(__file__) + '/data/goblint_' + property + '_timings.txt', delimiter=',', unpack=True, dtype=None)
    x2,y2,z2, firstrun, firstruntime, result, verdict = np.genfromtxt(os.path.dirname(__file__) + '/data/conflist_' + property + '_timings.txt', delimiter=',', unpack=True, dtype=None)
    _, newf, newft, newx = zip(*sorted(zip(z1,firstrun, firstruntime, x1)))
    new_z1, new_z2 = zip(*sorted(zip(z1,z2)))
    print("Goblint average: " + str(np.average(z1)))
    print("Conflist average: " + str(np.average(z2)))
    print("Goblint average 10 slowest: " + str(np.average(new_z1[-10:])))
    print("Conflist average 10 slowest: " + str(np.average(new_z2[-10:])))

    conf_true_correct = 0
    conf_false_correct = 0
    conf_true_incorrect = 0
    conf_false_incorrect = 0
    conf_unknown = result.tolist().count("unknown")
    conf_empty = result.tolist().count("empty")

    for i in range(len(result)):
        if result[i] == "True":
            if str(verdict[i]) == result[i]:
                conf_true_correct += 1
            else:
                conf_true_incorrect += 1
        elif result[i] == "False":
            if str(verdict[i]) == result[i]:
                conf_false_correct += 1
            else:
                conf_false_incorrect += 1

    print("Conflist correct true answers: " + str(conf_true_correct))
    print("Conflist correct false answers: " + str(conf_false_correct))
    print("Conflist incorrect true answers: " + str(conf_true_incorrect))
    print("Conflist incorrect false answers: " + str(conf_false_incorrect))
    print("Conflist unknown answers: " + str(conf_unknown))
    print("Conflist empty answers: " + str(conf_empty))


def conflist_expensive_stats(property):
    x1,y1,z1,_,_ = np.genfromtxt(os.path.dirname(__file__) + '/data/goblint_' + property + '_timings.txt', delimiter=',', unpack=True, dtype=None)
    x2,y2,z2, firstrun, firstruntime, result, verdict = np.genfromtxt(os.path.dirname(__file__) + '/data/conflist_expensive_' + property + '_timings.txt', delimiter=',', unpack=True, dtype=None)
    _, newf, newft, newx = zip(*sorted(zip(z1,firstrun, firstruntime, x1)))
    new_z1, new_z2 = zip(*sorted(zip(z1,z2)))
    print("Goblint average: " + str(np.average(z1)))
    print("Conflist average: " + str(np.average(z2)))
    print("Goblint average 10 slowest: " + str(np.average(new_z1[-10:])))
    print("Conflist average 10 slowest: " + str(np.average(new_z2[-10:])))

    conf_true_correct = 0
    conf_false_correct = 0
    conf_true_incorrect = 0
    conf_false_incorrect = 0
    conf_unknown = result.tolist().count("unknown")
    conf_empty = result.tolist().count("empty")

    for i in range(len(result)):
        if result[i] == "True":
            if str(verdict[i]) == result[i]:
                conf_true_correct += 1
            else:
                conf_true_incorrect += 1
        elif result[i] == "False":
            if str(verdict[i]) == result[i]:
                conf_false_correct += 1
            else:
                conf_false_incorrect += 1

    print("Conflist correct true answers: " + str(conf_true_correct))
    print("Conflist correct false answers: " + str(conf_false_correct))
    print("Conflist incorrect true answers: " + str(conf_true_incorrect))
    print("Conflist incorrect false answers: " + str(conf_false_incorrect))
    print("Conflist unknown answers: " + str(conf_unknown))
    print("Conflist empty answers: " + str(conf_empty))


def firstrun_toptime(property):
    x1,y1,z1,result,verdict = np.genfromtxt(os.path.dirname(__file__) + '/data/goblint_' + property + '_timings.txt', delimiter=',', unpack=True, dtype=None)
    x2,y2,z2, firstrun, firstruntime, _, _ = np.genfromtxt(os.path.dirname(__file__) + '/data/conflist_' + property + '_timings.txt', delimiter=',', unpack=True, dtype=None)
    _, newf, newft, newx = zip(*sorted(zip(z1,firstrun, firstruntime, x1)))
    print(newx[-10:])
    print(newf[-10:])
    print(np.average(newft[-10:]))
    test1,test2 = zip(*sorted(zip(z2,x2)))
    print(test1[-10:])
    print(test2[-10:])


def autotune_goblint_cumsum(property):
    x1,y1,z1,_,_ = np.genfromtxt(os.path.dirname(__file__) + '/data/goblint_' + property + '_timings.txt', delimiter=',', unpack=True, dtype=None)
    x2,y2,z2, _, _, _, _ = np.genfromtxt(os.path.dirname(__file__) + '/data/autotune_' + property + '_timings.txt', delimiter=',', unpack=True, dtype=None)
    new_z1, new_z2 = zip(*sorted(zip(z1,z2)))
    cum_z1 = np.cumsum(new_z1)
    cum_z2 = np.cumsum(new_z2)

    ax = plt.subplot(111)
    ax.set_title('Cumulative runtime for goblint-regression ' + property)
    ax.set_ylabel('Runtime in seconds')
    ax.set_xlabel('Analyzed file index')
    ax.plot(x1, cum_z1, color='g')
    ax.plot(x1, cum_z2, color='r')
    green_line = mlines.Line2D([], [], color='green', markersize=15, label='Goblint')
    red_line = mlines.Line2D([], [], color='red', markersize=15, label='Autotune')
    ax.legend(handles=[green_line, red_line])
    plt.savefig(os.path.dirname(__file__) + "/graphs/autotune_goblint_" + property + ".png")
    plt.clf()


def conflist_goblint_cumsum(property):
    x1,y1,z1,_,_ = np.genfromtxt(os.path.dirname(__file__) + '/data/goblint_' + property + '_timings.txt', delimiter=',', unpack=True, dtype=None)
    x2,y2,z2, _, _, _, _ = np.genfromtxt(os.path.dirname(__file__) + '/data/conflist_' + property + '_timings.txt', delimiter=',', unpack=True, dtype=None)
    new_z1, new_z2 = zip(*sorted(zip(z1,z2)))
    cum_z1 = np.cumsum(new_z1)
    cum_z2 = np.cumsum(new_z2)

    ax = plt.subplot(111)
    ax.set_title('Cumulative runtime for goblint-regression ' + property)
    ax.set_ylabel('Runtime in seconds')
    ax.set_xlabel('Analyzed file index')
    ax.plot(x1, cum_z1, color='g')
    ax.plot(x1, cum_z2, color='b')
    green_line = mlines.Line2D([], [], color='green', markersize=15, label='Goblint')
    blue_line = mlines.Line2D([], [], color='blue', markersize=15, label='Conflist')
    ax.legend(handles=[green_line, blue_line])
    plt.savefig(os.path.dirname(__file__) + "/graphs/conflist_goblint_" + property + ".png")
    plt.clf()


def conflist_expensive_goblint_cumsum(property):
    x1,y1,z1,_,_ = np.genfromtxt(os.path.dirname(__file__) + '/data/goblint_' + property + '_timings.txt', delimiter=',', unpack=True, dtype=None)
    x2,y2,z2, _, _, _, _ = np.genfromtxt(os.path.dirname(__file__) + '/data/conflist_expensive_' + property + '_timings.txt', delimiter=',', unpack=True, dtype=None)
    new_z1, new_z2 = zip(*sorted(zip(z1,z2)))
    cum_z1 = np.cumsum(new_z1)
    cum_z2 = np.cumsum(new_z2)

    ax = plt.subplot(111)
    ax.set_title('Cumulative runtime for goblint-regression ' + property)
    ax.set_ylabel('Runtime in seconds')
    ax.set_xlabel('Analyzed file index')
    ax.plot(x1, cum_z1, color='g')
    ax.plot(x1, cum_z2, color='b')
    green_line = mlines.Line2D([], [], color='green', markersize=15, label='Goblint')
    blue_line = mlines.Line2D([], [], color='blue', markersize=15, label='Conflist expensive')
    ax.legend(handles=[green_line, blue_line])
    plt.savefig(os.path.dirname(__file__) + "/graphs/conflist_expensive_goblint_" + property + ".png")
    plt.clf()


def main():

    #autotune_goblint_cumsum("no-data-race")
    #autotune_goblint_cumsum("no-overflow")
    #autotune_goblint_cumsum("unreach-call")

    #conflist_goblint_cumsum("no-data-race")
    #conflist_goblint_cumsum("no-overflow")
    #conflist_goblint_cumsum("unreach-call")

    #conflist_expensive_goblint_cumsum("no-data-race")
    #conflist_expensive_goblint_cumsum("no-overflow")
    #conflist_expensive_goblint_cumsum("unreach-call")

    #conflist_stats("no-data-race")
    #conflist_stats("no-overflow")
    #conflist_stats("unreach-call")

    conflist_expensive_stats("no-data-race")
    conflist_expensive_stats("no-overflow")
    conflist_expensive_stats("unreach-call")

    #goblint_stats("no-data-race")
    #goblint_stats("no-overflow")
    #goblint_stats("unreach-call")
    #firstrun_toptime("no-overflow")
    #autotune_time("no-data-race")
    return

if __name__ == "__main__":
    main()