import { ArrowLeft } from 'lucide-react'
import { Button } from '@/components/ui/button'
import { useNavigate } from 'react-router'
import { Label } from "@/components/ui/label"
import { Input } from "@/components/ui/input"
import { Textarea } from "@/components/ui/textarea"
import { useSettingsStore } from "@/stores/settingsStore"

export default function BrowseGames() {

    const navigate = useNavigate()
    const { age, interests, setAge, setInterests } = useSettingsStore()

    return (
    <div className='flex flex-col max-w-[800px] mx-auto p-8 gap-8'>
        <Button
          variant='outline'
          className='rounded-full w-fit'
          onClick={() => navigate('/browse')}
        >
          <ArrowLeft className='size-6' />
        </Button>
        <h1 className='text-4xl font-bold'>Settings</h1>
        <div className='flex flex-col gap-2'>
            <Label>Child's age</Label>
            <Input
              type='number'
              placeholder='e.g. 7'
              defaultValue={age}
              onBlur={(e) => {
                const parsed = parseInt(e.target.value, 10)
                setAge(Number.isNaN(parsed) ? 0 : parsed)
              }}
            />
        </div>
        <div className='flex flex-col gap-2'>
            <Label>Child's interests</Label>
            <Textarea
              placeholder='e.g. football, superheroes, volcanoes, dogs, cars'
              defaultValue={interests}
              onBlur={(e) => setInterests(e.target.value)}
            />
        </div>
    </div>
)
}