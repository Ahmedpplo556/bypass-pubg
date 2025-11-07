#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Encrypted by Smart Encryptor
# DO NOT MODIFY THIS FILE

import marshal
import base64
import zlib

__encrypted_data__ = b'c-pl&TW}NSdV7<!TCFaYWy`i~ytcVm7#rUJ+XRRMGI5NJkwGMbK^4;47Lg@ocMaA;sAtZLNtxIrr-Ry_(>l}4)Mwghl9!ft^1x|dI&%UQwPK4sJ`*}+rmu!Dla}<M-@m#oMi6qE%GU0G`TomyzbJ@lK4k9w?I@06bC?&CuydFfAH*eGeG?J^Z(@*qlai=<%u6~kN#~{DsrNd(IwuyvC4*NFecEe)r|~S~rF-7Su+UWutHr#=v&3j6_S~lzzLRzpf_X7SXbeG|Wg9TBsT<FZ*Jt|`oBHggzIjvMvZ-&~)VFQwmu>3XH}%VleJ|dGoi#RK-I#U+echGv4Q6aQAV}OBiFiO1InS&l1cFjb;99xCsKiGi;YmI!aRW2apcIZp^8nCf4#(mNAv`%Ham_(D*V*3L&Gnz3;l={*P6<qZB*J;oq{w-BkryuVA%;1^U*sdPI3ME9C;BwNK3))E$3Cv3t(_Th<BH*MYz9sjg1Cm_`m8um-|od!QNX=~m-JFzoman`jN?9h6n~ygJ`j#>BHIRp4YKnnFL6`+EL=h2MQ#F6jR&OQltK%<G$Ta)?Xt7IorC}WcFxnqb$Gae0j_g^^K=wIIsl}jGzb}u#br}*gATxkoa7}pp)l$>ekl>>6@%L5MG;+XJEz!1#05W}Cx2T!p;%#=Kf6Y~tH1!P4ZdQ#N`MVLW-L!RS~Ij=eVXUr-!M>C{oK(F24l+?_Fvn-D5siUTQMC-Q3t+76nKW7RGywwIeNzN@xtUN@jNXXu+z3YE#rib*pV9#sfywwMs?4xIfv&35k!sv4v=z1PKLPYKsd@x<RnY>G#}~<N2MzlW8u)1^RZauir)|Yz1{9{u?6P*{)vDn1p|=?^xcQVne+bUGwrRt{jCFm)`_z%0Jd|ydBjaBgup9$kq-#KRo$czn~B396^w;=g+*r~qJnTm72PzVu1Kmp-~=PQm5Lk>{3>Mrc0xJKRU_KFRbo9TKQni1owY0selWNgSz+CCo^K3n#_CwOeC=|w<BzVU=(_tRt6)Mz*OHRW6a6Cs?b8N?94{~>uc2{roGc1(o`7-6M-@okgGfGJAh@?c=C}?RVR)VqUc!g7U>|)HJSm?Jp1Mv$(MtHpQDX`9p)__xAJ>mF1p#483dkQ61jJCp%U3wZh7G&{bM)z-^}@&`iLe*~BK=;N&;?8kuYd_%gcv%4VMc5V=B4AtAH-;}fDtopE$qe=ZfWwFM$4XGndc>7Jc?nLU=QKCk3C29d|ANTf??0lq4NJs2cwULC(~*CQPl8eso_KFX_CA1>Y0~)k&8tm32s7&O>;<zxaLb?X(~1&aTfzZIB-6~i*5nQt85zWKY92~|FOY0nj2+Z<F3Z`S(${FT+!&>&vCnVbHhmG^Ug%(vi218`32f6m**FHRY>kIsK4xd5p+Wy`jixogr!8$Z8ami0e(j&X5DV1LW;bks<diT6@4Hc=c6Ho41_|08I2ew!qE^c5fGIW({xOf{K44tbS&yN3&;j5bR>M<9}P_Niut_iJN@w(m@84Sh&*339HL?@7!t*#vF1v7&Y7T_6)X~~859)?-A5@G!_)ByzX?z?C@Lm(E{L3_sOYk9gvWL;YlY7y`}WMOh3%@agMIU=an=Jz<=pUkMb*cr=0=|Av9j$;p%q)p+~79`+j`};r3)*S9rLCPU9m>j-lJ=imzR5%cYf}<<-X;*efVEYx8F~l45#WYr0I7vbmbadbC0e`_NM7=;Ido?Q<QVPyy9lxM}4U+9V_KMU`TD{i^o=N4f9mSWL-6FTd#31?_8<bGe4AJtJhfW9?LE5U!GmQa7%Y9bjx?U>-Oc_)2XqERKsMNoyxE^YwVVL?3Sdo%5HsR#L5~sESPIgiF54L$z3b<9dko)k*cOOXWKnz+p4qunhBk3TkQX^FS&KKru!Aomr^rwO1hl7{C=w8YMTAS=Ppv!vB6?&b&9IWIs&ct)#V+*-~685*M^-UXNWdzh8Wn1VefU7^1gW^ly@6BLsNqxv+xr55n^ap)+oe@IEf6y3{el?I2p#=gv^b_LA|oZ0Hi0ziF`aD1SFmlgF-kiiL$=+a(DZ#_uXVxopd5v051uq-BebCjJZ`YK{4dkDYz(7S#O*ZSF^g(pPLt2VeAMJ)Bda*wpGs!u3KyiQy)w%CRQvv=8oQPbgx+UeX=8Y;<MAgI{n!@*Aw&aEnK>G>BGb)Fq^XM%b4tQBme!F#H>9c(*9pM`^%_*aKIy|B?Xh`&)*u*NkwNiUf|6rRf2+eKJMxHIk@Sd>ZV`1;vBxKMq|`D<Pbtf(K;74Zg{m*H|?QD#`|(1#D3h5&k!@DzZhOXP*KV$6y|Y=s^PDj%)5x;zaKXjc5f)U4$Y{c<Y;MFjq`y3h&%_OjSFFGeeNbYpYCPOwIJ8!Y6MCF9n3{26fk8SZiqnh!<EAXItygKyo5{CX<XtU(vZUL7L|*|`)k~*mx8#K8FiM}k1RNFT(j1s35yC4;I!FJQnRZWLamo_9Kwoj6lD1fqtzusgF-sFN%Lz_FgEHcu|i*zT&*m{^+S8JmSDUtKlXMpG@&(^Sv8o^8q923%z)oUpRpAEwJGfjAT&wtczy9K$T5flRsJy-Z2k4i!?I0u0o=y90=*kcSzm9t&s4C#tdHH4{jj6kO6X<59t=}nhmT>gP9kpB(5%8|Mq?Vh^4nsk|E_SF#b+s;c0fJtRVe5#A(NJp`dF#qoJGSqr<QX=pJCcHRhpSEa}rXVZ7g|Cb;;2t?X7`>7NqyZ`DgUfmJ8f#;#RG7^jW>GSFm|4C1_S!cMBS>)%0g=q6ULnpLG)#i*t1v+5&c`Y&oBeu(Wx%_-wsJDTD;XX9M4x!xH?ht;h}S{>bWZSW8igRr?kOA6*Bt=+8qOYuZoNVPTxZiYbmB3)LV<NIHu*)SV=r-MtR>j}wOo)wZdvFdoJVyE!zw>CtXzg@+jWQw%FYz3gts{yYnniz#ej><8~y|6}gx-YT1iwY3EW7i8UxG|}1v)fk$OLf{gPPL9Z?GYw}sk08W^K2E_8Jl*!fTG;tSv0NqhF=uw3<wl_z!E=e&jF1h4rg(wp0?`l`7kIQ9)vq||QaH$SC_<88=RQVuFzC#YSauDMfcTJtGqQy_({dKloFE^*h!Pbm7YRq9Koy%%L7AsUNH|V;y4%DUL|3iQIe^x{MUL<iAC%A<Q!f5$7Tt_|Zujoi|HqHq26@(~5JP993~Mx7&;nW=<)b_b21CzM&HjAWrWnT5`}$=oLZm+$h$Lj-OdltgK?H~hl4AnGj^Wf?MMchurn7|1CNNOQn~8>ij00iV1=Sp9B9hoAJ0?&+Us!{Swn?*+f?txIIeM#boEShvmtt_T9bM&QOoCmqTZ3#E3yG~<qcU(H5RRw|)Ro)>^!hkA@f0{S#Yf^#iPkB3^uSO2kxwu`{gyxVj*PofAtQVga_j`kV1>zx3I#Ras6q*RAfy;Qvq3(tYNakN0DTo*I2xak1mv!SN;S3i93N1%QlTyY2NXtC9uZX?gk}WQs-_QobY@x=G&RQ%Ea-tENHv#L^uThI)9Wq?VTpH_DfmP-?ZA0Or>d4>;-}+MBAYfV6dDsy<O5{@VNyW8LSax^4V4bKpF)O1vrtx41y*5@Y4NM&L&d1JQ7J%hsnvq)0zVQ81&@d*3gI??ve^xVY6HS4Xbz#IriVnS#uFN&P1m~?dam{S?ES^}(uS&EjQz#ifAaQH;Fo7o?XRcnUf-Z}#`5*Dik}B>PTiPFzW2xPE_HqGTr2DSx~%usiHx)A=EWNqKb~Erz9TVvU#hJ4i3KxS=BKV(*J*RgvL{XNg+`%&EKLtTu-WHznM&up>4C+*K``dZb!Y9zmlmmv({)q6A>X|6(Upv&eyQVY$JWK6jI(hmkaq6KRMl;eSXDEm(@kjDR&kTP!6r|x+8V#3F<ZqtTb8oB)9lXsto?ztd?9fyk*rv;*3VOL@S^ooa>?_TO!7*qWq-=@TADrp``BD_Z?0SI3$xc}=gEx8vT*R)!DREAsVQx0$~bFoCT=8_%0Irk6!_ZN{K1=#beOH`34>W{lSfu84Rc2yQpWk?zc{>P__JflgUhukW^bC>2iw{mb8lrR%NkX2kE%#jUQAP$G~IzTb@ZW=TXHTptU7l=Ie^SqD;BO?yRvZggRA#h2b4f6t8TvY(L1U7?$0MyDh|vu-?Z#md~40I^`2wv(uuTV$F0-1$8LLW9hx^jM5rwplb2JLmNdN!)>gMIPpniOnm7NasVc)(uCaCZ*t*n~Y|S9oO-`rTU5H+eZJ!30TUWOCq_*|ma;5B^Rd(PZ8sD|bwmsU0Rkc3ZiRqa6)-+YMP8m~7O`38+Lml`JTa8NF`Ot@^M<iC}+Muy=H`F@_y{=>3T(;Pf6qir0nfH8c-gB!g!<rY4UOT#Y<mTXw!Q_P%2Vxb-jAbw2kg_!|yOu#b_NM85NKR~xpLTuGx3a_gMc;DZwktJy;$HuW&+ujZi@tk1yemy(sm7Bj%c)h`_uab$$Q{Tdh~D=PtyNDj0_2q~TO3-#lVZx=lxDa7j<tWkp@Z@7pR{3)+9w!puKca7VuOVD)9;|}X4wnZ{GZ2qta%LouXU3HAOHn)kCx^B<*t-v_Zr>)Z*=?juteAKR9pZJ`m$ws3-;?BWy6f_*F7|}|Ea5eM2G$JRtG$PW2zi!$9~h$FjA%air5D2uXY$mS}b4f(WB>nGmP9}Ov5hYoeB!p-f@xWxy3X>kaygc;REEI13GBm)tN>r$h!_4J*!M3&BnV;Xzks0({TrRcfaMhmHbz$4%!Os&;E?y7kZFkLZP0}i7KTA=9Czi<oo1aj*BOtni}Pv{{@IUgG>lAEN8hhS(guA)Q2G8tZZbCt9DdWcgfC=^bdQGc^QlI!SF-^Vu<rXKuB<C5!W2zCj#K^`nW<U;g%W3GaEpqMA)YBWtTxwNLx_e^TRM);jZCGXD}W|Axqawe=dZmp~Me{Zd^d&yWIKXy^!0i82tWFEC{4my~BRhG6!Q&1<uxG)yl3~{>>JGx91&;YK{@-5Y1ruYiR6sc>D@et9V(<O}{oB3(Z9MgTfi;qP@f~-~qCT<B#+Poch*|;mmI_=66{AW6FRZd~Da_wkNg*y!!C~uEWb8Th8Hl$Hwa<MzQm9nyk(ktczVYdv5fk4X&iLB>vUxC$s7L-S_hr8yfQy*Ujh!h1F_xd@xPFg$5#N+V#x9begVJ2RhSqm)h{8=>fHIWR>>(JI#Kmf8@fb8WpAg1vo{?>i'

def __load__():
    import sys
    import io
    try:
        # Fix encoding for Windows console
        if sys.platform == 'win32':
            sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
            sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')
        
        decoded = base64.b85decode(__encrypted_data__)
        decompressed = zlib.decompress(decoded)
        code_obj = marshal.loads(decompressed)
        exec(code_obj, {'__name__': '__main__', '__file__': __file__})
    except Exception as e:
        print(f"Error: Unable to execute encrypted code - {e}")
        exit(1)

if __name__ == "__main__":
    __load__()
