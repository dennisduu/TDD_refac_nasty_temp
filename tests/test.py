import io
import sys
from src import lessnasty
import pytest
def test_import():
    pass
#import the original nasty output for comparison
nasty_outputs = [
    """     0.00000000      0.00000000      0.00000000
     1.88495559      0.00000000      1.88495559
     3.76991118      3.55305758      1.21637590
     5.65486678      5.84587214     -7.20987045
     7.53982237     -7.74441349    -13.22663631
     9.42477796    -32.67603557     12.31208914
    11.30973355     -9.46829430     62.30109448
    13.19468915    107.96650214     22.95597165
    15.07964474    151.23748928   -200.39888460
    16.96460033   -226.50550891   -296.02085336
    18.84955592   -784.49167184    408.81710468

     0.00000000      0.00000000      0.00000000
     0.94247780      0.00000000      0.94247780
     1.88495559      0.88826440      1.33809946
     2.82743339      2.14939343      0.42434003
     3.76991118      2.54932448     -1.65394507
     4.71238898      0.99051797     -3.56846519
     5.65486678     -2.37268124     -3.48683923
     6.59734457     -5.65894979     -0.50385522
     7.53982237     -6.13382214      4.13614115
     8.48230016     -2.23560094      7.20554117
     9.42477796      4.55546162      5.48913818
    10.36725576      9.72885247     -1.39097868
    11.30973355      8.41788595     -9.47684689
    12.25221135     -0.51383181    -12.18217805
    13.19468915    -11.99526413     -5.02631248
    14.13716694    -16.73245205      9.54390123
    15.07964474     -7.73753705     21.48284070
    16.02212253     12.50956330     18.94298904
    16.96460033     30.36290987     -1.92110590
    17.90707813     28.55231021    -30.18614899
    18.84955592      0.10253504    -43.71093367

     0.00000000      0.00000000      0.00000000
     0.47123890      0.00000000      0.47123890
     0.94247780      0.22206610      0.81842438
     1.41371669      0.60773950      0.94081843
     1.88495559      1.05108974      0.79108568
     2.35619449      1.42388009      0.38636341
     2.82743339      1.60594955     -0.19532368
     3.29867229      1.51390544     -0.83236952
     3.76991118      1.12166054     -1.38663118
     4.24115008      0.46822599     -1.73410481
     4.71238898     -0.34895165     -1.79238394
     5.18362788     -1.19359268     -1.53884005
     5.65486678     -1.91875397     -1.01558932
     6.12610567     -2.39733916     -0.32028004
     6.59734457     -2.54826758      0.41511740
     7.06858347     -2.35264811      1.05271331
     7.53982237     -1.85656865      1.47796491
     8.01106127     -1.16009409      1.62337472
     8.48230016     -0.39509678      1.48151234
     8.95353906      0.30304946      1.10468621
     9.42477796      0.82362058      0.59158342
     9.89601686      1.10239770      0.06407281
    10.36725576      1.13259130     -0.36050813
    10.83849465      0.96270584     -0.59534849
    11.30973355      0.68215447     -0.60269207
    11.78097245      0.39814253     -0.40090354
    12.25221135      0.20922119     -0.05869514
    12.72345025      0.18156175      0.32197858
    13.19468915      0.33329058      0.63034143
    13.66592804      0.63033198      0.77293607
    14.13716694      0.99456952      0.69557756
    14.60840584      1.32235273      0.39622233
    15.07964474      1.50906810     -0.07405775
    15.55088364      1.47416921     -0.62211906
    16.02212253      1.18100251     -1.13324861
    16.49336143      0.64697168     -1.49648552
    16.96460033     -0.05823051     -1.62909797
    17.43583923     -0.82592484     -1.49479760
    17.90707813     -1.53033161     -1.11171917
    18.37831702     -2.05421693     -0.54850166
    18.84955592     -2.31269225      0.09054439

     0.00000000      0.00000000      0.00000000
     1.88495559      0.00000000      1.88495559
     3.76991118      3.55305758     -1.41653431
     5.65486678      0.88295332     -6.19635463
     7.53982237    -10.79689998     -1.43827246
     9.42477796    -13.50797970     18.74398330
    11.30973355     21.82359643     28.42509270
    13.19468915     75.40363387    -41.02639726
    15.07964474     -1.92930307   -143.90994681
    16.96460033   -273.19316208     -4.05888338
    18.84955592   -280.84397700    513.19854157

     0.00000000      0.00000000      0.00000000
     0.94247780      0.00000000      0.94247780
     1.88495559      0.88826440      0.20710394
     2.82743339      1.08345526     -1.49014152
     3.76991118     -0.32097003     -1.04658084
     4.71238898     -1.30734924      0.04035754
     5.65486678     -1.26931315      0.31100933
     6.59734457     -0.97619376      1.65199075
     7.53982237      0.58077084      2.55602995
     8.48230016      2.98977231      0.04168504
     9.42477796      3.02905954     -3.08699425
    10.36725576      0.11963600     -3.54462604
    11.30973355     -3.22109534     -2.27825631
    12.25221135     -5.36830132      1.06867697
    13.19468915     -4.36109701      6.38706016
    14.13716694      1.65856538      7.77870772
    15.07964474      8.98982469      1.60743923
    16.02212253     10.50480047     -7.33151716
    16.96460033      3.59500833    -13.01468173
    17.90707813     -8.67104023    -11.03235354
    18.84955592    -19.06878847      2.04754181

     0.00000000      0.00000000      0.00000000
     0.47123890      0.00000000      0.47123890
     0.94247780      0.22206610      0.63719312
     1.41371669      0.52233628      0.23679102
     1.88495559      0.63392142     -0.51332155
     2.35619449      0.39202434     -1.07234172
     2.82743339     -0.11330479     -1.00441427
     3.29867229     -0.58662386     -0.33312083
     3.76991118     -0.74360336      0.46998372
     4.24115008     -0.52212875      0.85528207
     4.71238898     -0.11908657      0.62282108
     5.18362788      0.17441095      0.06095165
     5.65486678      0.20313374     -0.31258625
     6.12610567      0.05583094     -0.18903854
     6.59734457     -0.03325137      0.27736773
     7.06858347      0.09745509      0.60892412
     7.53982237      0.38440382      0.41952512
     8.01106127      0.58210038     -0.24170947
     8.48230016      0.46819747     -0.90724118
     8.95353906      0.04067014     -1.05973120
     9.42477796     -0.45871642     -0.55221600
     9.89601686     -0.71894208      0.26530075
    10.36725576     -0.59392205      0.81857148
    10.83849465     -0.20817933      0.75995847
    11.30973355      0.14994266      0.23082484
    11.78097245      0.25871631     -0.27546107
    12.25221135      0.12890834     -0.33247428
    12.72345025     -0.02776647      0.06635678
    13.19468915      0.00350342      0.51198130
    13.66592804      0.24476893      0.53531843
    14.13716694      0.49703180      0.01685508
    14.60840584      0.50497457     -0.69257592
    15.07964474      0.17860585     -1.04434249
    15.55088364     -0.31352895     -0.73682029
    16.02212253     -0.66074733      0.03271077
    16.49336143     -0.64533275      0.71761359
    16.96460033     -0.30716531      0.85263577
    17.43583923      0.09462983      0.41524616
    17.90707813      0.29030998     -0.17536199
    18.37831702      0.20767258     -0.41646948
    18.84955592      0.01141597     -0.13921729
""", 
]
@pytest.mark.parametrize("expected_output", nasty_outputs)
def test_lessnasty_output(expected_output):
    captured_output = io.StringIO()
    sys.stdout = captured_output
    lessnasty.main()
    sys.stdout = sys.__stdout__
    actual_output = captured_output.getvalue().strip()
    expected_output = expected_output.strip()
    actual_output_lines = actual_output.split('\n')
    expected_output_lines = expected_output.split('\n')
    
    for actual_line, expected_line in zip(actual_output_lines, expected_output_lines):
        assert actual_line == expected_line, f"expect output: {expected_line}, but actual output was: {actual_line}"