"""Analytical teaching checks only. No EM solver or ADS simulation output.
Run: python reference_calculations.py
Uses only Python standard library; prints JSON. Do not submit as measured results.
"""
import math, cmath, json
from pathlib import Path

def theoretical_checks():
    c=299792458.0; f=2.45e9; er=4.4; h=.0016
    w=c/(2*f)*math.sqrt(2/(er+1))
    ee=(er+1)/2+(er-1)/2/math.sqrt(1+12*h/w)
    dl=.412*h*((ee+.3)*(w/h+.264))/((ee-.258)*(w/h+.8))
    l=c/(2*f*math.sqrt(ee))-2*dl
    lmatch=50/(2*math.pi*f); cmatch=1/(2*math.pi*f*100)
    zin=1/(1/100+1j*2*math.pi*f*cmatch)+1j*2*math.pi*f*lmatch
    assert abs(zin-50)<1e-10
    assert 0<l<.06 and 0<w<.06
    assert 10+2*.8<15  # SRR geometry is contained in the periodic cell
    a=.02286; b=.01016
    fc10=c/(2*a); fc20=c/a; fc01=c/(2*b)
    assert fc10<10e9<min(fc20,fc01)
    return {
      "kind":"analytical starting values only",
      "patch":{"W_mm":w*1000,"L_mm":l*1000,"epsilon_eff":ee,"delta_L_mm":dl*1000},
      "L_match":{"series_L_nH":lmatch*1e9,"shunt_C_pF":cmatch*1e12,"Zin_ohm":[zin.real,zin.imag]},
      "Wilkinson":{"Zbranch_ohm":50*math.sqrt(2),"phase_deg_at_f0":90,"Riso_ohm":100,"ideal_S21_dB":-10*math.log10(2)},
      "Butterworth_3GHz":{"series_L_nH":50/(2*math.pi*3e9)*1e9,"shunt_C_pF":2/(50*2*math.pi*3e9)*1e12},
      "WR90":{"TE10_cutoff_GHz":fc10/1e9,"next_air_mode_cutoff_GHz":min(fc20,fc01)/1e9}
    }

def check_s2p(path):
    ks=[]; mus=[]; gains=[]; freqs=[]
    for line in path.read_text(encoding="utf-8").splitlines():
        line=line.strip()
        if not line or line.startswith(("!","#")):continue
        q=[float(x) for x in line.split()]
        assert len(q)==9
        s11,s21,s12,s22=[complex(q[j],q[j+1]) for j in (1,3,5,7)]
        delta=s11*s22-s12*s21
        k=(1-abs(s11)**2-abs(s22)**2+abs(delta)**2)/(2*abs(s12*s21))
        mu=(1-abs(s11)**2)/(abs(s22-delta*s11.conjugate())+abs(s12*s21))
        ks.append(k);mus.append(mu);gains.append(20*math.log10(abs(s21)));freqs.append(q[0])
        assert k>1 and abs(delta)<1 and mu>1
    assert len(freqs)==61 and all(a<b for a,b in zip(freqs,freqs[1:]))
    assert max(abs(x-20) for x in gains)<1e-7
    return {"kind":"synthetic file consistency only","rows":len(freqs),"min_K":min(ks),"min_mu":min(mus),"S21_dB_range":[min(gains),max(gains)]}

def limiter_gain(pin_dBm,n=8192):
    # matched input voltage; matched output load halves open-circuit command
    pin_w=10**((pin_dBm-30)/10); vin_peak=math.sqrt(2*50*pin_w)
    fundamental=0.0
    for j in range(n):
        theta=2*math.pi*(j+.5)/n
        vo=math.tanh(20*vin_peak*math.sin(theta)/2)  # Vlim/2 = 1 V
        fundamental+=vo*math.sin(theta)
    vout_peak=2*fundamental/n
    pout_fundamental=vout_peak*vout_peak/(2*50)
    return 10*math.log10(pout_fundamental/pin_w)

def limiter_reference():
    g0=limiter_gain(-60); lo=-40;hi=0
    assert abs(g0-20)<.001 and limiter_gain(hi)<g0-1
    for _ in range(35):
        mid=(lo+hi)/2
        if limiter_gain(mid)>g0-1:lo=mid
        else:hi=mid
    p1=(lo+hi)/2
    assert abs(limiter_gain(p1,16384)-limiter_gain(p1,8192))<1e-6
    return {"kind":"ideal memoryless model analytical quadrature, not ADS HB","low_power_gain_dB":g0,"input_1dB_compression_dBm":p1,"gain_at_1dB_dB":limiter_gain(p1)}

if __name__=="__main__":
    result={"theory":theoretical_checks(),"s2p":check_s2p(Path(__file__).with_name("educational_active_2port.s2p")),"limiter":limiter_reference()}
    print(json.dumps(result,ensure_ascii=False,indent=2))
