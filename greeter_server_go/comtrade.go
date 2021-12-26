package main

import (
	"encoding/binary"
	"fmt"
	"io/ioutil"
	"os"
)

const TIMESTAMP_MISSING int32 = 0xFFFF

func getSamp(n int32, sampleRate [][]int32) float64 {
	lastSampleRate := 1.0
	if len(sampleRate) == 0 {
		panic("wrong sample rate")
	}
	for i := 0; i < len(sampleRate); i++ {
		samp := sampleRate[i][0]
		endsamp := sampleRate[i][1]
		if n <= endsamp {
			return float64(samp)
		}
	}
	return lastSampleRate
}

func getTime(n int32, tsValue int32, timeBase float64, timeMultiplier int32, timestampCritical bool, cfg_sample_rate [][]int32) float64 {
	sampleRate := getSamp(n, cfg_sample_rate)
	if (timestampCritical == false) || (tsValue == TIMESTAMP_MISSING) {
		if sampleRate != 0.0 {
			return float64(n-1) / sampleRate
		} else {
			panic("Missing timestamp and no sample rate provided.")
		}
	} else {
		return float64(tsValue) * timeBase * float64(timeMultiplier)
	}
}

func Parse(datFile string, timeMult int32, timeBase float64,
	achannels int32, schannels int32, a []float64, b []float64,
	groupsOf16bits int32, totalSamples int32,
	timestampCritical bool, cfgSampleRate [][]int32) ([][]float64, [][]int32, []float64) {
	allBytes, err := ioutil.ReadFile(datFile)
	if err != nil {
		fmt.Println(err)

	}

	analog := make([][]float64, achannels)
	for i := int32(0); i < achannels; i++ {
		analog[i] = make([]float64, totalSamples)
	}
	status := make([][]int32, schannels)
	for i := int32(0); i < schannels; i++ {
		status[i] = make([]int32, totalSamples)
	}
	t := make([]float64, totalSamples)

	irow := int32(0)
	var yint int16
	var group, mask uint16
	var n, ts_val, igroup, maxchn, ichannel, chnindex, extract int32
	var ts, y float64
	//var buff []byte

	//r:=Row{}
	//r.AnalogRowValue=make([]int32,achannels)
	//r.StatusRowValue=make([]int32,groups_of_16bits)
	rowLength := 8 + achannels*2 + groupsOf16bits*2
	for {
		if irow >= totalSamples {
			break
		}
		//buff:=make([]byte, 4+4+37*2+15*2)
		//err=binary.Read(fp,binary.LittleEndian,&buff)
		buff := allBytes[irow*rowLength : irow*rowLength+rowLength]

		//err=binary.Read(fp, binary.LittleEndian, &n)
		//err=binary.Read(fp, binary.LittleEndian, &ts_val)

		n = int32(binary.LittleEndian.Uint32(buff[0:4]))
		ts_val = int32(binary.LittleEndian.Uint32(buff[4:8]))
		//err=binary.Read(fp,binary.LittleEndian,&r)
		if err != nil {
			fmt.Println(err)
		}
		ts = getTime(n, ts_val, timeBase, int32(timeMult), timestampCritical, cfgSampleRate)
		t[irow] = ts

		for ichannel = 0; ichannel < achannels; ichannel++ {
			//err=binary.Read(fp, binary.LittleEndian, &yint)
			yint = int16(binary.LittleEndian.Uint16(buff[8+ichannel*2 : 8+ichannel*2+2]))
			y = a[ichannel]*float64(yint) + b[ichannel]
			analog[ichannel][irow] = y
		}

		for igroup = 0; igroup < groupsOf16bits; igroup++ {
			//err=binary.Read(fp, binary.LittleEndian, &group)
			group = binary.LittleEndian.Uint16(buff[8+achannels*2+igroup*2 : 8+achannels*2+igroup*2+2])
			if (igroup+1)*16 > schannels {
				maxchn = schannels
			} else {
				maxchn = (igroup + 1) * 16
			}
			for ichannel = igroup * 16; ichannel < maxchn; ichannel++ {
				chnindex = ichannel - igroup*16
				mask = 1 << chnindex
				extract = int32((group & mask) >> chnindex)
				status[ichannel][irow] = extract
			}
		}
		irow++
	}

	return analog, status, t

}

func Test() ([][]float64,[][]int32,[]float64) {
	OneDrive := os.Getenv("OneDrive")
	var a = []float64{0.0077882301786596, 0.0077882301786596, 0.0077882301786596, 0.0233633191997365, 0.001953125, 0.0017452006980803, 0.0017452006980803, 0.0017452006980803, 0.0052356020942408, 0.0017452006980803, 0.0017452006980803, 0.0017452006980803, 0.0052356020942408, 0.0017452006980803, 0.0017452006980803, 0.0017452006980803, 0.0052356020942408, 0.0017452006980803, 0.0017452006980803, 0.0017452006980803, 0.0052356020942408, 0.0017452006980803, 0.0017452006980803, 0.0017452006980803, 0.0052356020942408, 0.0017452006980803, 0.0017452006980803, 0.0017452006980803, 0.0052356020942408, 9.25925925926e-05, 9.25925925926e-05, 9.25925925926e-05, 0.0002777777777778, 9.25925925926e-05, 9.25925925926e-05, 9.25925925926e-05, 0.0002777777777778}
	var b = []float64{0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0}
	var sampleRate = [][]int32{{10000, 68060}}
	analog,status,t:=Parse(OneDrive+"\\cgy\\01-工作记录\\20210619 数字化大赛\\算法4.电容器塔不平衡电流\\res\\录波文件\\216\\38957.DAT",
		1.0,
		1e-6,
		37,
		232,
		a,
		b,
		15,
		68060,
		false,
		sampleRate,
	)
	//fmt.Println(analog,status,t)
	return analog,status,t
}

