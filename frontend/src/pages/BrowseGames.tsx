import { ArrowRight } from 'lucide-react'
import { useNavigate } from 'react-router'
import { Button } from '@/components/ui/button'

export default function BrowseGames() {

    const navigate = useNavigate()

    const games = [
        {name: 'Sound stories', description: 'Exciting tales filled with the special sound you\'re practicing.', path: '/games/sound-stories'},
        {name: 'Wh Questions', description: 'Test your understanding of a story with these fun questions.', path: '/games/wh-questions'},
    ]

    return (
    <div className='flex flex-col justify-center max-w-[1000px] mx-auto p-8 gap-8'>
        <div className='flex flex-row justify-between items-center'>
            <h1 className='text-4xl font-bold'>Browse games</h1>
            <Button className='rounded-full' variant='outline' onClick={() => navigate('/settings')}>Settings</Button>
        </div>
        <div className='flex flex-col gap-4'>
            {games.map((game) => (
            <button key={game.name} 
                className='flex flex-row justify-between border rounded-lg p-4 cursor-pointer hover:bg-muted text-left items-center' 
                onClick={() => navigate(game.path)}
            >
                <div className='flex flex-col'>
                <div className='text-base font-bold'>{game.name}</div>
                <div className='text-sm text-muted-foreground'>{game.description}</div>
                </div>
                <ArrowRight />
            </button>
            ))}
        </div>
    </div>
)
}