import { Button } from '@/components/ui/button'
import { ArrowRight } from 'lucide-react'
import { useNavigate } from 'react-router'

export default function LandingPage() {
  const navigate = useNavigate()

  return (
    <div className='flex flex-col items-center justify-center h-screen gap-8'>
      <h1 className='text-6xl font-bold text-center'>Language exercises<br />that feel like play, not practice</h1>
      <Button className='mt-4' onClick={() => navigate('/browse')}>Explore games <ArrowRight /></Button>
    </div>
  )
}