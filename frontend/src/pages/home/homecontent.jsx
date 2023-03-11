

function Home() {


    //Need all cards to have the same dimensions
    return (
        <div id = "home-content" className="flex items-center justify-center gap-10 h-80v">
        
            <div className="w-80 h-160 rounded overflow-hidden shadow-lg">
                <img className="w-full" src="https://images.immediate.co.uk/production/volatile/sites/4/2021/08/mountains-7ddde89.jpg?quality=90&resize=768,574"/>
                <div className="px-6 py-6">
                    <h1 className="font-bold text-xl mb-2">
                        Random Title
                    </h1>
                    <p className="text-gray-700 text-base">
                        paowrntawipntawtawtawiotboiawtlnawgoib
                    </p>
                </div>
                <div id="tags" className="px-6 py-6">
                    <span class="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2">#photography</span>
                    <span class="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2">#travel</span>
                    <span class="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2">#winter</span>
                </div>
            </div>

            <div className="w-80 h-160 rounded overflow-hidden shadow-lg">
                <img className="w-full" src="https://cdn.britannica.com/67/19367-050-885866B4/Valley-Taurus-Mountains-Turkey.jpg"/>
                <div className="px-6 py-6">
                    <h1 className="font-bold text-xl mb-2">
                        Random Title
                    </h1>
                    <p className="text-gray-700 text-base">
                        paowrntawipntawtawtawiotboiawtlnawgoib
                    </p>
                </div>
                <div id="tags" className="px-6 py-6">
                    <span class="inline-block bg-gray-200 rounded-full px-2 py-1 text-xs font-semibold text-gray-700 mr-2 mb-2">#photography</span>
                    <span class="inline-block bg-gray-200 rounded-full px-2 py-1 text-xs font-semibold text-gray-700 mr-2 mb-2">#travel</span>
                    <span class="inline-block bg-gray-200 rounded-full px-2 py-1 text-xs font-semibold text-gray-700 mr-2 mb-2">#winter</span>
                </div>
            </div>
        </div>
    )
}

export default Home