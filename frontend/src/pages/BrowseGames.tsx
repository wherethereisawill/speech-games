import { ArrowRight } from 'lucide-react'
import { useNavigate } from 'react-router'

export default function BrowseGames() {

    const navigate = useNavigate()

    return (
    <div className='flex flex-col justify-center max-w-[1000px] mx-auto p-8 gap-8'>
    <h1 className='text-4xl font-bold'>Browse games</h1>
    <button 
        className='flex flex-row justify-between border rounded-lg p-4 cursor-pointer hover:bg-muted text-left items-center' 
        onClick={() => navigate('/games/sound-stories')}
    >
        <div className='flex flex-col'>
        <div className='text-base font-bold'>Sound stories</div>
        <div className='text-sm text-muted-foreground'>Exciting tales filled with the special sound you're practicing.</div>
        </div>
        <ArrowRight />
    </button>
    </div>
)
}