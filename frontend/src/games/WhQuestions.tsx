import TopBar from "@/components/ui/TopBar"
import { Button } from "@/components/ui/button"
import { useEffect, useRef, useState } from "react"
import { useSettingsStore } from "@/stores/settingsStore"

export default function SoundStories() {

    const gameStates = ['ready', 'loading', 'reading', 'who', 'what', 'when', 'where', 'why', 'how', 'done'] as const;
    type GameState = typeof gameStates[number];

    const [currentState, setCurrentState] = useState<GameState>('ready');
    const audioRef = useRef<HTMLAudioElement | null>(null)

    type WhQsResponse = {
        scene_description: string
        who: string
        what: string
        when: string
        where: string
        why: string
        how: string
        image_base64: string
        audio: {
            scene_description: string
            who: string
            what: string
            when: string
            where: string
            why: string
            how: string
        }
    }

    const [whData, setWhData] = useState<WhQsResponse | null>(null)

    const stageSequence: GameState[] = ['reading', 'who', 'what', 'when', 'where', 'why', 'how', 'done']

    const stateToAudioKey: Partial<Record<GameState, keyof WhQsResponse['audio']>> = {
        reading: 'scene_description',
        who: 'who',
        what: 'what',
        when: 'when',
        where: 'where',
        why: 'why',
        how: 'how',
    }

    const getQuestionText = (state: GameState, data: WhQsResponse | null): string | null => {
        if (!data) return null
        switch (state) {
            case 'who':
                return data.who
            case 'what':
                return data.what
            case 'when':
                return data.when
            case 'where':
                return data.where
            case 'why':
                return data.why
            case 'how':
                return data.how
            default:
                return null
        }
    }

    const handleStartGame = async () => {
        const { age, interests } = useSettingsStore.getState()
        setCurrentState('loading')
        try {
            const params = new URLSearchParams({
                age: String(age),
                interests,
            })
            const res = await fetch(`http://0.0.0.0:8000/create-wh-q?${params.toString()}`)
            if (!res.ok) throw new Error(`Request failed: ${res.status}`)
            const data = (await res.json()) as WhQsResponse
            console.log('WH Qs response:', data)
            setWhData(data)
            setCurrentState('reading')
        } catch (err) {
            console.error('Failed to fetch WH questions:', err)
        }
    }

    useEffect(() => {
        const key = stateToAudioKey[currentState]
        if (!key || !whData) return
        try {
            if (audioRef.current) {
                audioRef.current.pause()
                audioRef.current.src = ''
            }
            const audio = new Audio(whData.audio[key])
            audioRef.current = audio
            // play after user interaction (button click) should be allowed
            void audio.play()
        } catch (e) {
            console.error('Audio playback failed:', e)
        }
    }, [currentState, whData])

    const handleNext = () => {
        const idx = stageSequence.indexOf(currentState)
        if (idx === -1) return
        const next = stageSequence[Math.min(idx + 1, stageSequence.length - 1)]
        setCurrentState(next)
    }

    return (
        <div className="min-h-screen flex flex-col">
            <TopBar title="Wh Questions" />
            {currentState === 'ready' && (
                <div className="flex-1 flex flex-col items-center justify-center w-full gap-4">
                    <h1 className="text-2xl font-bold">Ready to practice your Wh questions?</h1>
                    <Button onClick={handleStartGame}>Start game!</Button>
                </div>
            )}
            {currentState === 'loading' && (
                <div className="flex-1 flex flex-col items-center justify-center w-full gap-4">
                    <h1 className="text-2xl font-bold">Loading...</h1>
                </div>
            )}
            {whData && (
                <div className="flex-1 grid grid-cols-1 md:grid-cols-2 gap-6 px-6 py-4 items-stretch">
                    <div className="flex flex-col gap-6 justify-center h-full">
                        <div className="space-y-3">
                            {/* <h2 className="text-2xl md:text-3xl font-semibold">Story</h2> */}
                            <p className="text-2xl md:text-3xl leading-relaxed whitespace-pre-line">
                                {whData.scene_description}
                            </p>
                        </div>
                        <div className="space-y-2 min-h-16">
                            {getQuestionText(currentState, whData) && (
                                <>
                                    <h3 className="text-xl md:text-2xl font-medium capitalize">{currentState} question</h3>
                                    <p className="text-xl md:text-2xl">{getQuestionText(currentState, whData)}</p>
                                </>
                            )}
                            {currentState === 'done' && (
                                <p className="text-xl md:text-2xl font-medium">Great job! You're all done.</p>
                            )}
                        </div>
                        {currentState !== 'done' && (
                            <div>
                                <Button onClick={handleNext}>Next</Button>
                            </div>
                        )}
                    </div>
                    <div className="flex justify-center md:justify-end items-center h-full w-full">
                        <img src={whData.image_base64} alt="WH scene" className="w-full h-full object-cover rounded-md shadow" />
                    </div>
                </div>
            )}
        </div>
    )
  }