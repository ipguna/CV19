# CV19

Simple simulation on COVID-19 number of cases projection in Indonesia.

Content:
- [Objective](#objective)
- [Data](#data)
- [Mathematical model](#mathematical-model)
- [Sample of results](#sample-of-results)
    + [Using original parameters](#using-original-parameters)
    + [Using modified parameters](#using-modified-parameters)
- [Discussions](#discussions)


## Objective

At first instance, originally this was an attempt to find mathematical model
to the rate of change of number of COVID-19 cases in Indonesia as it progresses. However, it turns out that some preliminary results was already published in `[1]`,
and accordingly the original purpose was slightly shifted into replicating
the results in \[1]\, and if possible, do some refinements to the model.


## Data

Data source: http://kcov.id/daftarpositif

    Original data from the website was downloaded in csv format.
    CSV filename: daily.csv
    Data was read in from the csv file

## Mathematical model

The mathematical model was taken from http://eprints.itb.ac.id/119/

<img src="https://latex.codecogs.com/gif.latex?y&space;=&space;\dfrac{K}{&space;\left(1&space;&plus;&space;\alpha&space;e^{-r(t-t_m)}&space;\right)^{1/\alpha}&space;}" title="y = \dfrac{K}{ \left(1 + \alpha e^{-r(t-t_m)} \right)^{1/\alpha} }" />


\[1\] Nuraini, Nuning and Khairudin, Kamal and Apri, Mochamad
Data dan Simulasi COVID-19 dipandang dari Pendekatan Model Matematika.
Preprint. (Submitted)

## Sample of results

### Using original parameters

The following results was obtained by using the original parameters for
 Korean model given in \[1\]. As we can see both from the figure as well
 as from the RMSE value, the results using this parameter model
 is inadequate.

    K = 8495    r = 0.2000      alpha = 0.41000     t_m = 40.1200   RMSE = 359.110836

![Result with Korean parameters](results/cv19caseID_Korean_20200319001.png "Result with Korean parameters")


### Using modified parameters

In light of the inadequate results from using the original parameters
(Korean model) given in the reference, different values for the parameter
was used. We can see some improvement in terms of the RMSE value, reflected
by the closeness of the predicted model with respect to the actual data
in the graph.

The following results and graphs were obtained by running the simulation
on 20200319; i.e., 16 days after the first public outbreak of COVID-19 in
Indonesia:

    K = 8495    r = 0.2000      alpha = 1.07654    t_m = 40.1200   RMSE = 71.122767

![Result with modified parameters](results/cv19caseID_Modified_20200319001.png "Result with modified parameters")

<!--

# TODO: Include more recent results

-->

### Discussions

Not really sure why the original parameters given in the paper failed to
replicate the same results. There is, however, a possibility that using
different dataset resource will result in discrepancies with the original
results presented in \[1\].



### Notes

Mathematical equations was typeset in LaTeX using online renderer in
[CodeDogs editor](https://www.codecogs.com/latex/eqneditor.php).

