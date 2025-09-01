import { Button } from "@/components/ui/button"
import { Separator } from "@/components/ui/separator"
import { ArrowLeft } from "lucide-react"
import { useNavigate } from "react-router"

interface TopBarProps {
  title?: React.ReactNode
}

export default function TopBar({ title }: TopBarProps) {
  const navigate = useNavigate()

  return (
    <div>
      <div className='relative flex items-center justify-center w-full p-4'>
        <Button
          variant='outline'
          className='absolute left-4 rounded-full'
          onClick={() => navigate('/browse')}
        >
          <ArrowLeft className='size-6' />
        </Button>
        <h1 className='font-bold text-center w-full'>
          {title ?? 'Title'}
        </h1>
      </div>
      <Separator />
    </div>
  )
}