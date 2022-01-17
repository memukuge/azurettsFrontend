
import streamlit as st
import trans


langs = ["アフリカーンス語	af","アルバニア語	sq","アムハラ語	am","アラビア語	ar","アルメニア語	hy","アッサム語	as","アゼルバイジャン語	az","ベンガル語	bn","ボスニア語 (ラテン)	bs","ブルガリア語	bg","広東語 (繁体字)	yue","カタロニア語	ca","簡体中国語	zh-Hans","中国語 (繁体字)	zh-Hant","クロアチア語	hr","チェコ語	cs","デンマーク語	da","ダリー語	prs","オランダ語	nl","英語	en","エストニア語	et","フィジー語	fj","フィリピン語	fil","フィンランド語	fi","フランス語	fr","フランス語 (カナダ)	fr-ca","ドイツ語	de","ギリシャ語	el","グジャラート語	gu","ハイチ・クレオール語	ht","ヘブライ語	he","ヒンディー語	hi","ミャオ語	mww","ハンガリー語	hu","アイスランド語	is","インドネシア語	id","イヌクティトット語	iu","アイルランド語	ga","イタリア語	it","日本語	ja","カンナダ語	kn","カザフ語	kk","クメール語	km","韓国語	ko","クルド語 (中央)	ku","クルド語 (北)	kmr","ラオス語	lo","ラトビア語	lv","リトアニア語	lt","マダガスカル語	mg","マレー語	ms","マラヤーラム語	ml","マルタ語	mt","マオリ語	mi","マラーティー語	mr","ミャンマー	my","ネパール語	ne","ノルウェー語	nb","オディア語	or","パシュトウ語	ps","ペルシャ語	fa","ポーランド語	pl","ポルトガル語 (ブラジル)	pt","ポルトガル語 (ポルトガル)	pt-pt","パンジャーブ語	pa","オトミ語	otq","ルーマニア語	ro","ロシア語	ru","セルビア語 (キリル)	sr-Cyrl","セルビア語 (ラテン)	sr-Latn","スロバキア語	sk","スロベニア語	sl","スペイン語	es","スワヒリ語	sw","スウェーデン語	sv","タミル語	ta","テルグ語	te","ティグリニア語	ti","トンガ語	to","トルコ語	tr","ウクライナ語	uk","ウルドゥ語	ur","ベトナム語	vi","ウェールズ語	cy"]


st.title('Azure Cognitive Text Translation App')
st.write('MS社のテキスト翻訳。これは社外にテキストが出ます。')

langfrom = st.selectbox('language translate FROM',langs)
langto = st.selectbox('language translate TO',langs)

txt = st.text_area("翻訳したい文章", value="", height=10)

answer = st.button('翻訳')
    
if answer == True:
    st.write('翻訳中、しばらくお待ちください')
    lf = langfrom.split(sep="\t")[1]
    lt = langto.split(sep="\t")[1]
    #st.write(lf)
    #st.write(lt)    

    output = trans.late(lf,lt,txt)
    st.write(output)
else:
    st.write('翻訳押したらここに訳文表示')